import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *

from UI.ui_gss_reg import *
from imp1 import gss_reg

from os import environ

class gss_page_show():
    def __init__(self):
        self.gss_page = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.gss_page)
        
        self.ui.drone_btn.clicked.connect(self.reg_gss)
    
    def reg_gss(self):
        gss_list,pubgss = gss_reg(str(self.ui.Name_edt.text()))
        self.ui.pubid.setText(str(pubgss))
        
    def show(self):
        self.gss_page.show()