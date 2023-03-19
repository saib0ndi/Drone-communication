import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *

from UI.ui_LandingPage import *

from Control_room_page import Control_room
from secure_drone import *

from os import environ

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Ctrl_btn.clicked.connect(self.show_ctrl_room)
        self.ui.drone_btn.clicked.connect(self.show_dron)
        self.show()
    
    
    def show_dron(self):
        self.dr = sec_drone()
        self.dr.show()
        
        
    def show_ctrl_room(self):
        self.control_page = Control_room()
        self.control_page.show() 
        #self.hide()

if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    
    window = MainWindow()
    sys.exit(app.exec_())
