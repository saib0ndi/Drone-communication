import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *

from UI.d2d_connect import *
from imp1 import *

from os import environ

class d2d_coo():
    def __init__(self,from_drone_id):
        self.gss_page = QMainWindow()
        self.ui = Ui_d2d()
        self.ui.setupUi(self.gss_page)
        self.from_drone_id = from_drone_id
        
        self.ui.drone_btn.clicked.connect(self.check)
    
    
    def check(self):
        success = check_conn_stat(str(self.ui.Name_edt.text()))
        if success:
            end_conn_drone(self.from_drone_id)
            #end_conn_gss(self.from_drone_id)
            p = d2d(self.from_drone_id,str(self.ui.Name_edt.text()))
            
            self.ui.label_3.setText(str(p))
        else:
            self.ui.label_3.setText("Connection unavailable!!")
      
    def show(self):
        self.gss_page.show()
