<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="ja_JP">
  <context>
    <name>TXT2TIFDialogBase</name>
    <message><source>txt2tif DEM builder</source><translation>txt2tif DEM builder</translation></message>
    <message><source>Input</source><translation>入力</translation></message>
    <message><source>Single File</source><translation>単一ファイル</translation></message>
    <message><source>Folder</source><translation>フォルダ</translation></message>
    <message><source>Input Path</source><translation>入力パス</translation></message>
    <message><source>Columns</source><translation>列設定</translation></message>
    <message><source>X column</source><translation>X列</translation></message>
    <message><source>Y column</source><translation>Y列</translation></message>
    <message><source>Z column</source><translation>Z列</translation></message>
    <message><source>Delimiter</source><translation>区切り文字</translation></message>
    <message><source>Custom Delimiter</source><translation>その他区切り</translation></message>
    <message><source>Skip Rows</source><translation>スキップ行数</translation></message>
    <message><source>CRS</source><translation>CRS</translation></message>
    <message><source>Coordinate Reference System</source><translation>座標参照系</translation></message>
    <message><source>Output</source><translation>出力</translation></message>
    <message><source>Output for Single-File Input</source><translation>単一ファイル入力時の出力</translation></message>
    <message><source>Output File</source><translation>出力ファイル</translation></message>
    <message><source>Output for Folder Input</source><translation>フォルダ入力時の出力</translation></message>
    <message><source>Output Individual TIFFs</source><translation>個別tifを出力</translation></message>
    <message><source>Output Merged TIFF</source><translation>マージtifを出力</translation></message>
    <message><source>Folder for Individual Outputs</source><translation>個別出力先フォルダ</translation></message>
    <message><source>Merged Output File</source><translation>マージ出力ファイル名</translation></message>
    <message><source>Open output file(s) after running algorithm</source><translation>アルゴリズムの終了後に出力ファイルを開く</translation></message>
    <message><source>Run</source><translation>実行</translation></message>
    <message><source>Cancel</source><translation>キャンセル</translation></message>
    <message><source>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name="qrichtext" content="1" /&gt;&lt;style type="text/css"&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=" font-family:'MS UI Gothic'; font-size:9.216pt; font-weight:400; font-style:normal;"&gt;
&lt;h3 style=" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;&lt;span style=" font-size:large; font-weight:600;"&gt;Create GeoTIFF from txt/csv&lt;/span&gt;&lt;/h3&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;This tool creates a GeoTIFF by using the specified x, y, and z coordinate columns.&lt;/p&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;&lt;span style=" font-weight:600;"&gt;Input methods&lt;/span&gt;&lt;/p&gt;
&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;"&gt;&lt;li style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;Single file input&lt;/li&gt;
&lt;li style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;Folder input&lt;/li&gt;&lt;/ul&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;&lt;span style=" font-weight:600;"&gt;Main features&lt;/span&gt;&lt;/p&gt;
&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;"&gt;&lt;li style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;Convert txt/csv to GeoTIFF&lt;/li&gt;
&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;Output multiple files in a folder individually&lt;/li&gt;
&lt;li style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;Merge multiple TIFF files into one output&lt;/li&gt;&lt;/ul&gt;
&lt;p style=" margin-top:12px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;Input point coordinates are interpreted as the centers of output raster cells.&lt;/p&gt;
&lt;p style=" margin-top:6px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;The NoData value is set to -9999.&lt;/p&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;Set the delimiter and the number of skipped rows according to the input file format.&lt;/p&gt;
&lt;p style=" margin-top:24px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;GitHub: &lt;a href="https://github.com/Mizuki011124/txt_2_tif_dem_builder"&gt;https://github.com/Mizuki011124/txt_2_tif_dem_builder&lt;/a&gt;&lt;/p&gt;
&lt;/body&gt;&lt;/html&gt;</source><translation>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name="qrichtext" content="1" /&gt;&lt;style type="text/css"&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=" font-family:'MS UI Gothic'; font-size:9.216pt; font-weight:400; font-style:normal;"&gt;
&lt;h3 style=" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;&lt;span style=" font-size:large; font-weight:600;"&gt;txt/csv から GeoTIFF を作成&lt;/span&gt;&lt;/h3&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;指定した x、y、z座標列を用いてGeoTIFFを作成します。&lt;/p&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;&lt;span style=" font-weight:600;"&gt;入力方法&lt;/span&gt;&lt;/p&gt;
&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;"&gt;&lt;li style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;単一ファイル入力&lt;/li&gt;
&lt;li style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;フォルダ入力&lt;/li&gt;&lt;/ul&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;&lt;span style=" font-weight:600;"&gt;主な機能&lt;/span&gt;&lt;/p&gt;
&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;"&gt;&lt;li style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;txt/csv を GeoTIFF に変換&lt;/li&gt;
&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;フォルダ内の複数ファイルを個別に出力&lt;/li&gt;
&lt;li style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;複数の tif をマージして出力&lt;/li&gt;&lt;/ul&gt;
&lt;p style=" margin-top:12px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;入力点の座標は、出力ラスタセルの中心に対応するように処理します。&lt;/p&gt;
&lt;p style=" margin-top:6px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;nodata値は -9999 が割り当てられます。&lt;/p&gt;
&lt;p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;区切り文字とスキップ行数は、入力ファイル形式に合わせて設定してください。&lt;/p&gt;
&lt;p style=" margin-top:24px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"&gt;GitHub: &lt;a href="https://github.com/Mizuki011124/txt_2_tif_dem_builder"&gt;https://github.com/Mizuki011124/txt_2_tif_dem_builder&lt;/a&gt;&lt;/p&gt;
&lt;/body&gt;&lt;/html&gt;
</translation></message>
  </context>
  <context>
    <name>TXT2TIFDialog</name>
    <message><source>Text/CSV (*.txt *.csv);;All files (*.*)</source><translation>Text/CSV (*.txt *.csv);;すべてのファイル (*.*)</translation></message>
    <message><source>GeoTIFF (*.tif *.tiff)</source><translation>GeoTIFF (*.tif *.tiff)</translation></message>
    <message><source>Space</source><translation>スペース</translation></message>
    <message><source>Comma (,)</source><translation>カンマ (,)</translation></message>
    <message><source>Tab (	)</source><translation>タブ (	)</translation></message>
    <message><source>Semicolon (;)</source><translation>セミコロン (;)</translation></message>
    <message><source>Other</source><translation>その他</translation></message>
    <message><source>Stop</source><translation>中止</translation></message>
    <message><source>Please specify an input path.</source><translation>入力パスを指定してください。</translation></message>
    <message><source>When &quot;Other&quot; is selected, please enter a delimiter character.</source><translation>「その他」を選択した場合は、区切り文字を入力してください。</translation></message>
    <message><source>Please specify different column numbers for X, Y, and Z.</source><translation>X列・Y列・Z列には異なる列番号を指定してください。</translation></message>
    <message><source>The specified input file was not found.</source><translation>指定された入力ファイルが見つかりません。</translation></message>
    <message><source>Please specify an output file name.</source><translation>出力ファイル名を指定してください。</translation></message>
    <message><source>The specified input folder was not found.</source><translation>指定された入力フォルダが見つかりません。</translation></message>
    <message><source>For folder input, select either &quot;Output individual TIFFs&quot; or &quot;Output merged TIFF&quot;.</source><translation>フォルダ入力時は「個別TIFFを出力」または「マージTIFFを出力」を選択してください。</translation></message>
    <message><source>Please specify an output folder for individual files.</source><translation>個別出力先フォルダを指定してください。</translation></message>
    <message><source>Please specify an output file name for the merged TIFF.</source><translation>マージ出力ファイル名を指定してください。</translation></message>
    <message><source>Input Error</source><translation>入力エラー</translation></message>
    <message><source>Processing was canceled.</source><translation>処理を中止しました。</translation></message>
    <message><source>Canceled</source><translation>中止</translation></message>
    <message><source>Processing completed.</source><translation>処理が完了しました。</translation></message>
    <message><source>Completed</source><translation>完了</translation></message>
    <message><source>Error</source><translation>エラー</translation></message>
    <message><source>No txt/csv files were found in the input folder.</source><translation>入力フォルダ内に txt / csv ファイルが見つかりません。</translation></message>
    <message><source>Empty File</source><translation>空ファイルの確認</translation></message>
    <message><source>{filename} is empty.

Do you want to skip this file and continue processing?</source><translation>{filename} は空のファイルです。

このファイルをスキップして処理を続行しますか？</translation></message>
    <message><source>Skipped empty file: {filename}</source><translation>空ファイルをスキップしました: {filename}</translation></message>
    <message><source>Processing was stopped because an empty file was included.</source><translation>空のファイルが含まれているため、処理を中止しました。</translation></message>
    <message><source>{filename} is an empty file.</source><translation>{filename} は空のファイルです。</translation></message>
    <message><source>{filename} does not have enough columns. Specified columns: X={x_col}, Y={y_col}, Z={z_col}, Actual number of columns: {actual_cols}</source><translation>{filename} の列数が不足しています。指定列: X={x_col}, Y={y_col}, Z={z_col}, 実際の列数: {actual_cols}</translation></message>
    <message><source>Created: {path}</source><translation>作成: {path}</translation></message>
    <message><source>There are no TIFF files to merge.</source><translation>マージ対象の TIFF がありません。</translation></message>
    <message><source>Failed to create VRT.</source><translation>VRT の作成に失敗しました。</translation></message>
    <message><source>Merged: {path}</source><translation>マージ完了: {path}</translation></message>
    <message><source>Added to QGIS layer: {path}</source><translation>QGIS レイヤに追加: {path}</translation></message>
    <message><source>Failed to add layer: {path}</source><translation>レイヤ追加に失敗: {path}</translation></message>
  </context>
</TS>
