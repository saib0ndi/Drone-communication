# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secure_dronewKklHR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class sec_drone_ui(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 516)
        MainWindow.setStyleSheet(u"background-color: rgb(237, 205, 187);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 71))
        self.label.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 100, 761, 241))
        self.Ctrl_btn = QPushButton(self.centralwidget)
        self.Ctrl_btn.setObjectName(u"Ctrl_btn")
        self.Ctrl_btn.setGeometry(QRect(60, 390, 261, 41))
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
        self.Ctrl_btn_2 = QPushButton(self.centralwidget)
        self.Ctrl_btn_2.setObjectName(u"Ctrl_btn_2")
        self.Ctrl_btn_2.setGeometry(QRect(490, 390, 261, 41))
        self.Ctrl_btn_2.setStyleSheet(u"QPushButton {\n"
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Secured Drone Communication", None))
        self.Ctrl_btn.setText(QCoreApplication.translate("MainWindow", u"Establish d2d Connections", None))
        self.Ctrl_btn_2.setText(QCoreApplication.translate("MainWindow", u"Establish d2g Connections", None))
    # retranslateUi

