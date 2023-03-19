import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *

from UI.ui_secure_drone import *

from os import environ
from imp1 import *
from d2d_con import *

class sec_drone():
    def __init__(self):
        self.gss_page = QMainWindow()
        self.ui = sec_drone_ui()
        self.ui.setupUi(self.gss_page)
        
        self.ui.tableWidget.setRowCount(50);
        self.ui.tableWidget.setColumnCount(1);
        self.columnLabels = ["Drone ID"]
        self.ui.tableWidget.setHorizontalHeaderLabels(self.columnLabels)
        #function
        results = ret_drone()
        row_2 = 0
        for each in results:
            transaction_at = QTableWidgetItem(str(each[0]))
            msg = QTableWidgetItem(transaction_at)
            self.ui.tableWidget.setItem(row_2,0,msg)
            row_2 = row_2 + 1
        self.ui.Ctrl_btn.clicked.connect(self.show_d2d)
        self.ui.Ctrl_btn_2.clicked.connect(self.show_g2g)
    
    def show_d2d(self):
        row = self.ui.tableWidget.currentRow()
        from_drone = self.ui.tableWidget.item(row,0).text()
        self.d2d_c = d2d_coo(from_drone)
        self.d2d_c.show()
        #self.gss_page.hide()
    
    def show_g2g(self):
        row = self.ui.tableWidget.currentRow()
        from_drone = self.ui.tableWidget.item(row,0).text()
        end_conn_drone(from_drone)
        #end_conn_gss(from_drone)
        d2g(from_drone)
    
    
    def show(self):
        self.gss_page.show()
