#######################################################
#           GHOST PHISHER FONT SETTINGS               #
#######################################################

from PyQt5 import QtCore, QtGui, QtWidgets


import os
cwd = os.getcwd()

from .settings import *

settings_object = Ghost_settings()

class Ui_font_settings(object):
    def setupUi(self, font_settings):
        font_settings.setObjectName("font_settings")
        font_settings.resize(318, 121)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("%s/gui/images/icon.png"%(cwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font_settings.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(font_settings)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 300, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.layoutWidget1 = QtWidgets.QWidget(font_settings)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 300, 38))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget1)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.layoutWidget2 = QtWidgets.QWidget(font_settings)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 40, 301, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.font_combo = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_combo.sizePolicy().hasHeightForWidth())
        self.font_combo.setSizePolicy(sizePolicy)
        self.font_combo.setObjectName("font_combo")
        self.horizontalLayout_2.addWidget(self.font_combo)
        self.retranslateUi(font_settings)
        self.buttonBox.accepted.connect(font_settings.accept)
        self.buttonBox.rejected.connect(font_settings.reject)
        QtCore.QMetaObject.connectSlotsByName(font_settings)

    def retranslateUi(self, font_settings):
        font_settings.setWindowTitle(QtCore.QCoreApplication.translate("font_settings", "Ghost Font Settings", None))
        self.label.setText(QtCore.QCoreApplication.translate("font_settings", "Current font:", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("font_settings", "Font:", None))


class font_settings(QtWidgets.QDialog,Ui_font_settings):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.label.setText('Current font:<font color=green><b>\t %s</b></font>'%(settings_object.read_last_settings('font-settings')))
        font_numbers = []
        for iterate in range(1,21):
            font_numbers.append(str(iterate))

        self.font_combo.addItems(font_numbers)

        self.buttonBox.accepted.connect(self.set_font)

    def set_font(self):
        ''' Writes font settings to last_setting'''
        prefered_font = str(self.font_combo.currentText())
        settings_object.create_settings('font-settings',prefered_font)
        settings_object.close_setting_file()
        self.close()

        QtWidgets.QMessageBox.information(self,"Font Changes","Please restart application to apply changes")
