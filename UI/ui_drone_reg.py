# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drone_registrationDrocDl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class drone_reg_ui(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(781, 490)
        MainWindow.setStyleSheet(u"background-color: rgb(237, 205, 187);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 781, 71))
        self.label.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.Name_edt = QLineEdit(self.centralwidget)
        self.Name_edt.setObjectName(u"Name_edt")
        self.Name_edt.setGeometry(QRect(410, 180, 281, 31))
        self.Name_edt.setStyleSheet(u"color: rgb(0,0,0);\n"
"font: 75 10pt \"Goudy Old Style\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 170, 221, 51))
        self.label_2.setStyleSheet(u"font: italic 10pt \"Goudy Old Style\";")
        self.drone_btn = QPushButton(self.centralwidget)
        self.drone_btn.setObjectName(u"drone_btn")
        self.drone_btn.setGeometry(QRect(310, 310, 201, 31))
        self.drone_btn.setStyleSheet(u"QPushButton {\n"
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Drone Registration", None))
        self.Name_edt.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Drone ID", None))
        self.drone_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

