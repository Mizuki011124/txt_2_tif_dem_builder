# -*- coding: utf-8 -*-
"""
TXT2TIF plugin entry
"""
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .resources import *
from .txt_2_tif_dem_builder_dialog import TXT2TIFDialog

import os.path


class TXT2TIF:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)

        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(self.plugin_dir, 'i18n', 'TXT2TIF_{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.actions = []
        self.menu = self.tr(u'&txt2tif DEM builder')

    def tr(self, message):
        return QCoreApplication.translate('TXT2TIF', message)

    def add_action(self, icon_path, text, callback, enabled_flag=True,
                   add_to_menu=True, add_to_toolbar=True,
                   status_tip=None, whats_this=None, parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        if add_to_toolbar:
            self.iface.addToolBarIcon(action)
        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        icon_path = ':/plugins/txt_2_tif_dem_builder/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'txt2tif DEM builder'),
            callback=self.run,
            parent=self.iface.mainWindow()
        )

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(self.tr(u'&txt2tif DEM builder'), action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        dlg = TXT2TIFDialog(self.iface.mainWindow())
        dlg.reset_form()
        dlg.show()
        dlg.raise_()
        dlg.activateWindow()
        dlg.exec_()
