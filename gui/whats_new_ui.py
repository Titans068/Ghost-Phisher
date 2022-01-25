# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAVIOUR\Desktop\untitled.ui'
#
# Created: Tue May 08 11:50:19 2012
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Dialog.resize(638, 324)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        # self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.verticalLayout = QtWidgets.QVBoxLayout()
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.webView = QWebView(Dialog)
        # self.webView.setObjectName("webView")
        # self.verticalLayout.addWidget(self.webView)
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        self.whats_new_check = QtWidgets.QCheckBox(Dialog)
        self.whats_new_check.setObjectName("whats_new_check")
        self.verticalLayout_2.addWidget(self.whats_new_check)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout.addItem(spacerItem)
        # self.verticalLayout.addLayout(self.horizontalLayout)
        # self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Whats New", None))
        self.whats_new_check.setText(QtCore.QCoreApplication.translate("Dialog", "Dont show again until next update", None))

try:
    from PyQt5.QtWebKitWidgets import QWebView
except:
    pass