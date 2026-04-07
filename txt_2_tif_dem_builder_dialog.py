# -*- coding: utf-8 -*-
"""
TXT2TIFDialog
"""

import glob
import os
import traceback

import numpy as np
from osgeo import gdal, osr

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QApplication, QMessageBox
from qgis.core import (
    Qgis,
    QgsCoordinateReferenceSystem,
    QgsMessageLog,
    QgsProject,
    QgsRasterLayer,
)
from qgis.gui import QgsFileWidget

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), 'txt_2_tif_dem_builder_dialog_base.ui')
)


class TXT2TIFDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(TXT2TIFDialog, self).__init__(parent)
        self.setupUi(self)

        self._is_running = False
        self._cancel_requested = False

        self._setup_widgets()
        self._connect_signals()
        self.reset_form()

    # ------------------------------
    # UI 初期化
    # ------------------------------
    def _setup_widgets(self):
        self.fileWidgetInput.setFilter('Text/CSV (*.txt *.csv);;All files (*.*)')
        self.fileWidgetSingleOutput.setFilter('GeoTIFF (*.tif *.tiff)')
        self.fileWidgetMergedOutput.setFilter('GeoTIFF (*.tif *.tiff)')

        self.fileWidgetInput.setStorageMode(QgsFileWidget.GetFile)
        self.fileWidgetSingleOutput.setStorageMode(QgsFileWidget.SaveFile)
        self.fileWidgetOutputFolder.setStorageMode(QgsFileWidget.GetDirectory)
        self.fileWidgetMergedOutput.setStorageMode(QgsFileWidget.SaveFile)

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setFormat('%p%')

    def _connect_signals(self):
        self.radioInputFile.toggled.connect(self._update_input_mode_ui)
        self.radioInputFolder.toggled.connect(self._update_input_mode_ui)
        self.checkOutputIndividual.toggled.connect(self._update_output_mode_ui)
        self.checkOutputMerged.toggled.connect(self._update_output_mode_ui)
        self.comboDelimiter.currentIndexChanged.connect(self._update_delimiter_ui)
        self.pushButtonRun.clicked.connect(self.on_run_clicked)
        self.pushButtonCancel.clicked.connect(self.on_cancel_clicked)

    def reset_form(self):
        self._is_running = False
        self._cancel_requested = False

        self.radioInputFile.setChecked(True)
        self.fileWidgetInput.setStorageMode(QgsFileWidget.GetFile)
        self.fileWidgetInput.setFilePath('')

        self.spinXcol.setValue(1)
        self.spinYcol.setValue(2)
        self.spinZcol.setValue(3)

        self.comboDelimiter.setCurrentIndex(0)
        self.lineEditCustomDelimiter.clear()
        self.spinSkipRows.setValue(0)

        default_crs = QgsCoordinateReferenceSystem('EPSG:4326')
        if default_crs.isValid():
            self.crsSelector.setCrs(default_crs)

        self.fileWidgetSingleOutput.setFilePath('')
        self.checkOutputIndividual.setChecked(True)
        self.checkOutputMerged.setChecked(False)
        self.fileWidgetOutputFolder.setFilePath('')
        self.fileWidgetMergedOutput.setFilePath('')

        if hasattr(self, 'checkAddToQgis'):
            self.checkAddToQgis.setChecked(True)

        self.progressBar.setValue(0)
        self._set_running_state(False)
        self._update_input_mode_ui()
        self._update_output_mode_ui()
        self._update_delimiter_ui()

    def _update_input_mode_ui(self):
        is_file = self.radioInputFile.isChecked()

        if is_file:
            self.fileWidgetInput.setStorageMode(QgsFileWidget.GetFile)
            self.fileWidgetInput.setFilter('Text/CSV (*.txt *.csv);;All files (*.*)')
        else:
            self.fileWidgetInput.setStorageMode(QgsFileWidget.GetDirectory)

        self.labelSingleOutputHeader.setEnabled(is_file)
        self.labelSingleOutput.setEnabled(is_file)
        self.fileWidgetSingleOutput.setEnabled(is_file)

        is_folder = not is_file
        self.labelFolderOutputHeader.setEnabled(is_folder)
        self.checkOutputIndividual.setEnabled(is_folder)
        self.checkOutputMerged.setEnabled(is_folder)
        self.labelOutputFolder.setEnabled(is_folder and self.checkOutputIndividual.isChecked())
        self.fileWidgetOutputFolder.setEnabled(is_folder and self.checkOutputIndividual.isChecked())
        self.labelMergedOutput.setEnabled(is_folder and self.checkOutputMerged.isChecked())
        self.fileWidgetMergedOutput.setEnabled(is_folder and self.checkOutputMerged.isChecked())

    def _update_output_mode_ui(self):
        is_folder = self.radioInputFolder.isChecked()
        enable_individual = is_folder and self.checkOutputIndividual.isChecked()
        enable_merged = is_folder and self.checkOutputMerged.isChecked()

        self.labelOutputFolder.setEnabled(enable_individual)
        self.fileWidgetOutputFolder.setEnabled(enable_individual)
        self.labelMergedOutput.setEnabled(enable_merged)
        self.fileWidgetMergedOutput.setEnabled(enable_merged)

    def _update_delimiter_ui(self):
        self.lineEditCustomDelimiter.setEnabled(self.comboDelimiter.currentText() == 'その他')

    def _set_running_state(self, running):
        self._is_running = running
        self.groupBoxInput.setEnabled(not running)
        self.groupBoxColumns.setEnabled(not running)
        self.groupBoxCRS.setEnabled(not running)
        self.groupBoxOutput.setEnabled(not running)
        self.pushButtonRun.setEnabled(not running)
        self.pushButtonCancel.setText('中止' if running else 'キャンセル')

    # ------------------------------
    # 値取得・検証
    # ------------------------------
    def _get_delimiter(self):
        text = self.comboDelimiter.currentText()
        if text == 'スペース':
            return None
        if text == 'カンマ (,)':
            return ','
        if text == 'タブ (\\t)':
            return '\t'
        if text == 'セミコロン (;)':
            return ';'
        if text == 'その他':
            return self.lineEditCustomDelimiter.text()
        return ','

    def _get_params(self):
        crs = self.crsSelector.crs()
        authid = crs.authid() if crs.isValid() else 'EPSG:4326'
        epsg = int(authid.split(':')[1]) if authid.startswith('EPSG:') else 4326
        return {
            'input_mode': 'file' if self.radioInputFile.isChecked() else 'folder',
            'input_path': self.fileWidgetInput.filePath().strip(),
            'x_col': self.spinXcol.value(),
            'y_col': self.spinYcol.value(),
            'z_col': self.spinZcol.value(),
            'delimiter': self._get_delimiter(),
            'skiprows': self.spinSkipRows.value(),
            'epsg': epsg,
            'single_output': self.fileWidgetSingleOutput.filePath().strip(),
            'output_individual': self.checkOutputIndividual.isChecked(),
            'output_merged': self.checkOutputMerged.isChecked(),
            'output_folder': self.fileWidgetOutputFolder.filePath().strip(),
            'merged_output': self.fileWidgetMergedOutput.filePath().strip(),
            'nodata': -9999.0,
            'add_to_qgis': self.checkAddToQgis.isChecked() if hasattr(self, 'checkAddToQgis') else True,
        }

    def _ensure_tif_extension(self, path):
        if path and not path.lower().endswith(('.tif', '.tiff')):
            return path + '.tif'
        return path

    def _validate_params(self, params):
        if not params['input_path']:
            raise ValueError('入力パスを指定してください。')
        if params['delimiter'] == '':
            raise ValueError('その他区切りを選んだ場合は、区切り文字を入力してください。')
        if len({params['x_col'], params['y_col'], params['z_col']}) < 3:
            raise ValueError('X列・Y列・Z列には異なる列番号を指定してください。')

        if params['input_mode'] == 'file':
            if not os.path.isfile(params['input_path']):
                raise ValueError('指定された入力ファイルが見つかりません。')
            if not params['single_output']:
                raise ValueError('出力ファイル名を指定してください。')
            params['single_output'] = self._ensure_tif_extension(params['single_output'])
        else:
            if not os.path.isdir(params['input_path']):
                raise ValueError('指定された入力フォルダが見つかりません。')
            if not params['output_individual'] and not params['output_merged']:
                raise ValueError('フォルダ入力時は「個別tifを出力」または「マージtifを出力」を選択してください。')
            if params['output_individual'] and not params['output_folder']:
                raise ValueError('個別出力先フォルダを指定してください。')
            if params['output_merged']:
                if not params['merged_output']:
                    raise ValueError('マージ出力ファイル名を指定してください。')
                params['merged_output'] = self._ensure_tif_extension(params['merged_output'])

    # ------------------------------
    # 実行
    # ------------------------------
    def on_run_clicked(self):
        if self._is_running:
            return
        try:
            params = self._get_params()
            self._validate_params(params)
        except Exception as e:
            QMessageBox.warning(self, '入力エラー', str(e))
            return

        self._cancel_requested = False
        self.progressBar.setValue(0)
        self._set_running_state(True)

        try:
            added_paths = []
            if params['input_mode'] == 'file':
                added_paths = self._run_single_file(params)
            else:
                added_paths = self._run_folder(params)

            if self._cancel_requested:
                self._log('処理を中止しました。', Qgis.Warning)
                QMessageBox.information(self, '中止', '処理を中止しました。')
                return

            if params['add_to_qgis']:
                for tif_path in added_paths:
                    self._add_raster_to_project(tif_path)

            self.progressBar.setValue(100)
            self._log('処理が完了しました。', Qgis.Success)
            QMessageBox.information(self, '完了', '処理が完了しました。')
            self.accept()

        except Exception as e:
            self._log(traceback.format_exc(), Qgis.Critical)
            QMessageBox.critical(self, 'エラー', str(e))
        finally:
            self._set_running_state(False)

    def on_cancel_clicked(self):
        if self._is_running:
            self._cancel_requested = True
        else:
            self.reject()

    def _run_single_file(self, params):
        self._txt_to_tif(
            txt_path=params['input_path'],
            out_tif=params['single_output'],
            x_col=params['x_col'],
            y_col=params['y_col'],
            z_col=params['z_col'],
            epsg=params['epsg'],
            delimiter=params['delimiter'],
            skiprows=params['skiprows'],
            nodata=params['nodata'],
        )
        self.progressBar.setValue(100)
        return [params['single_output']]


    def _run_folder(self, params):
        patterns = ['*.txt', '*.csv']
        input_files = []
        for pattern in patterns:
            input_files.extend(glob.glob(os.path.join(params['input_path'], pattern)))
        input_files = sorted(set(input_files))

        if not input_files:
            raise ValueError('入力フォルダ内に txt / csv ファイルが見つかりません。')

        generated_tifs = []
        added_paths = []
        total_steps = len(input_files) + (1 if params['output_merged'] else 0)
        current_step = 0

        temp_output_folder = params['output_folder']
        cleanup_temp_outputs = not params['output_individual']
        if cleanup_temp_outputs:
            temp_output_folder = os.path.join(params['input_path'], '_tmp_txt2tif_outputs')

        os.makedirs(temp_output_folder, exist_ok=True)

        try:
            for txt_path in input_files:
                if self._cancel_requested:
                    break

                name = os.path.splitext(os.path.basename(txt_path))[0]
                out_tif = os.path.join(temp_output_folder, name + '.tif')

                try:
                    self._txt_to_tif(
                        txt_path=txt_path,
                        out_tif=out_tif,
                        x_col=params['x_col'],
                        y_col=params['y_col'],
                        z_col=params['z_col'],
                        epsg=params['epsg'],
                        delimiter=params['delimiter'],
                        skiprows=params['skiprows'],
                        nodata=params['nodata'],
                    )
                except ValueError as e:
                    if '空のファイル' in str(e):
                        reply = QMessageBox.question(
                            self,
                            '空ファイルの確認',
                            f'{os.path.basename(txt_path)} は空のファイルです。\n\n'
                            'このファイルをスキップして処理を続行しますか？',
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No,
                        )
                        if reply == QMessageBox.Yes:
                            self._log(
                                '空ファイルをスキップしました: {}'.format(os.path.basename(txt_path)),
                                Qgis.Warning,
                            )
                            current_step += 1
                            self._set_progress_by_steps(current_step, total_steps)
                            continue
                        raise ValueError('空のファイルが含まれているため、処理を中止しました。')
                    raise

                generated_tifs.append(out_tif)
                current_step += 1
                self._set_progress_by_steps(current_step, total_steps)

            if self._cancel_requested:
                return []

            if params['output_individual']:
                added_paths.extend(generated_tifs)

            if params['output_merged']:
                self._merge_tifs(generated_tifs, params['merged_output'], nodata=params['nodata'])
                current_step += 1
                self._set_progress_by_steps(current_step, total_steps)
                added_paths.append(params['merged_output'])

            return added_paths

        finally:
            if cleanup_temp_outputs:
                for tif_path in generated_tifs:
                    try:
                        if os.path.exists(tif_path):
                            os.remove(tif_path)
                    except OSError:
                        pass
                try:
                    if os.path.isdir(temp_output_folder) and not os.listdir(temp_output_folder):
                        os.rmdir(temp_output_folder)
                except OSError:
                    pass

    # ------------------------------
    # 変換本体
    # ------------------------------

    def _txt_to_tif(self, txt_path, out_tif, x_col, y_col, z_col, epsg=4326,
                    nodata=-9999.0, delimiter=',', skiprows=0):
        try:
            data = np.loadtxt(txt_path, delimiter=delimiter, skiprows=skiprows)
            if data.ndim == 1:
                data = np.expand_dims(data, axis=0)

            if data.size == 0:
                raise ValueError(f'{os.path.basename(txt_path)} は空のファイルです。')

            max_col = max(x_col, y_col, z_col)
            if data.shape[1] < max_col:
                raise ValueError(
                    f'{os.path.basename(txt_path)} の列数が不足しています。'
                    f' 指定列: X={x_col}, Y={y_col}, Z={z_col}, 実際の列数: {data.shape[1]}'
                )

            x = data[:, x_col - 1]
            y = data[:, y_col - 1]
            z = data[:, z_col - 1]

            xs = np.unique(x)
            ys = np.unique(y)
            xs.sort()
            ys.sort()

            nx = xs.size
            ny = ys.size
            x_res = xs[1] - xs[0] if nx > 1 else 0.5
            y_res = ys[1] - ys[0] if ny > 1 else 0.5

            grid = np.full((ny, nx), nodata, dtype=np.float32)
            ix = np.searchsorted(xs, x)
            iy = np.searchsorted(ys, y)
            rows = ny - 1 - iy
            cols = ix
            grid[rows, cols] = z

            x_min = xs.min()
            y_max = ys.max()
            geotransform = (
                x_min - x_res / 2.0,
                x_res,
                0.0,
                y_max + y_res / 2.0,
                0.0,
                -y_res,
            )

            os.makedirs(os.path.dirname(out_tif), exist_ok=True) if os.path.dirname(out_tif) else None
            driver = gdal.GetDriverByName('GTiff')
            ds = driver.Create(out_tif, nx, ny, 1, gdal.GDT_Float32)
            ds.SetGeoTransform(geotransform)

            srs = osr.SpatialReference()
            srs.ImportFromEPSG(epsg)
            ds.SetProjection(srs.ExportToWkt())

            band = ds.GetRasterBand(1)
            band.WriteArray(grid)
            band.SetNoDataValue(nodata)
            band.FlushCache()
            ds = None
            self._log('作成: {}'.format(out_tif), Qgis.Info)
            QApplication.processEvents()

        except Exception:
            try:
                if os.path.exists(out_tif):
                    os.remove(out_tif)
            except OSError:
                pass
            raise

    def _merge_tifs(self, tif_list, out_tif_path, nodata=-9999.0):
        if not tif_list:
            raise ValueError('マージ対象の tif がありません。')

        vrt_path = os.path.splitext(out_tif_path)[0] + '.vrt'
        vrt = gdal.BuildVRT(vrt_path, tif_list, srcNodata=nodata, VRTNodata=nodata)
        if vrt is None:
            raise RuntimeError('VRT の作成に失敗しました。')

        gdal.Translate(out_tif_path, vrt, format='GTiff', noData=nodata)
        vrt = None
        try:
            os.remove(vrt_path)
        except OSError:
            pass
        self._log('マージ完了: {}'.format(out_tif_path), Qgis.Info)
        QApplication.processEvents()

    # ------------------------------
    # 補助
    # ------------------------------
    def _set_progress_by_steps(self, current_step, total_steps):
        if total_steps <= 0:
            self.progressBar.setValue(0)
        else:
            self.progressBar.setValue(int(current_step * 100 / total_steps))
        QApplication.processEvents()

    def _add_raster_to_project(self, tif_path):
        if not tif_path or not os.path.exists(tif_path):
            return
        layer_name = os.path.splitext(os.path.basename(tif_path))[0]
        raster = QgsRasterLayer(tif_path, layer_name)
        if raster.isValid():
            QgsProject.instance().addMapLayer(raster)
            self._log('QGIS レイヤに追加: {}'.format(tif_path), Qgis.Info)
        else:
            self._log('レイヤ追加に失敗: {}'.format(tif_path), Qgis.Warning)

    def _log(self, message, level=Qgis.Info):
        QgsMessageLog.logMessage(message, 'txt2tif DEM builder', level)
