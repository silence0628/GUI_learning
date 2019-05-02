# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from hhh import Ui_MainWindow
import requests
import os
from PIL import Image
import numpy as np
import numpy as np
import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QFrame,QGridLayout,QLabel,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt,QTimer



from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signal_func() # 初始化信号槽函数，
        
        self.Fs = 1024.0 #采样频率
        self.N = 1024    #采样点数
        self.f0 = 4.0    #信号频率
        self.pha = 0     #初始相位
        self.t = np.arange(self.N) / self.Fs    #时间向量 1*1024的矩阵

    #链接信号槽函数
    def signal_func(self):
        self.ui.pushButton.clicked.connect(self.Print) #启动按钮单击显示图片

    def Print(self):
        self.ui.label.setData(self.t , np.sin(8 * np.pi  * self.t+ self.pha * np.pi/180.0))


if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())