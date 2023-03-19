import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *

from UI.ui_control_room import *
from drone_reg_page import *
from gss_reg import gss_page_show
from os import environ

class Control_room():
    def __init__(self):
        self.controlroom = QMainWindow()
        self.ui = control_room_ui()
        self.ui.setupUi(self.controlroom)
        self.ui.Ctrl_btn.clicked.connect(self.Drone_reg_page)
        self.ui.Ctrl_btn_3.clicked.connect(self.Gss_reg_page)
    
    
    def Drone_reg_page(self):
        self.drone_page = drone_page()
        self.drone_page.show()
        #self.controlroom.hide()
    
    
    def Gss_reg_page(self):
        self.gss_pge = gss_page_show()
        self.gss_pge.show()
        #self.controlroom.hide()
    
    def show(self):
        self.controlroom.show()
