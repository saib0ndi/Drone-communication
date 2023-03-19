# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Control_room_pagegwCXSx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class control_room_ui(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 484)
        MainWindow.setStyleSheet(u"background-color: rgb(237, 205, 187);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 801, 71))
        self.label.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.Ctrl_btn = QPushButton(self.centralwidget)
        self.Ctrl_btn.setObjectName(u"Ctrl_btn")
        self.Ctrl_btn.setGeometry(QRect(270, 200, 281, 41))
        self.Ctrl_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(237, 188, 160);\n"
"font: italic 10pt \"Goudy Old Style\";\n"
"	\n"
"color: rgb(0,0,0);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 233, 206);\n"
"color:rgb(0,0,0);\n"
"}")
        self.Ctrl_btn_3 = QPushButton(self.centralwidget)
        self.Ctrl_btn_3.setObjectName(u"Ctrl_btn_3")
        self.Ctrl_btn_3.setGeometry(QRect(270, 270, 281, 41))
        self.Ctrl_btn_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(237, 188, 160);\n"
"font: italic 10pt \"Goudy Old Style\";\n"
"	\n"
"color: rgb(0,0,0);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 233, 206);\n"
"color:rgb(0,0,0);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Control Room", None))
        self.Ctrl_btn.setText(QCoreApplication.translate("MainWindow", u"Drone Registration", None))
        self.Ctrl_btn_3.setText(QCoreApplication.translate("MainWindow", u"GSS Registration", None))
    # retranslateUi

