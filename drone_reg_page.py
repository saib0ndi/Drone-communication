import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *

from UI.ui_drone_reg import *

from os import environ
from imp1 import dr_reg

class drone_page():
    def __init__(self):
        self.drone_page = QMainWindow()
        self.ui = drone_reg_ui()
        self.ui.setupUi(self.drone_page)
        self.ui.drone_btn.clicked.connect(self.drone_Reg)
    
    def drone_Reg(self):
        success = dr_reg(str(self.ui.Name_edt.text()))
        print(success)
       
    def show(self):
        self.drone_page.show()