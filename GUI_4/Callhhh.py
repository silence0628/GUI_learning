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
import time


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signal_func() # 初始化信号槽函数，
        
        self.Fs = 1024.0 #采样频率
        self.N = 4096    #采样点数
        self.f0 = 4.0    #信号频率
        self.pha = 0     #初始相位
        self.t = np.arange(self.N)  #时间向量 1*4096的矩阵

        self.draw = QPainter()  # 绘制类实例
        self.picture = QPixmap(981, 451)  # 设置图片大小
        self.data = self.load_data()
        self.end_dot_list = [[0, 0]]  # 保存绘制点位列表
        self.beg_x = 0
        self.beg_y = 0

        self.x_num = 4096 #X轴分成多少等份
        self.y_num = 1000 #Y轴分成多少等份

        self.x_num1 = 981/self.x_num #每一等份的宽度
        self.y_num1 = 451/self.y_num #每一等份的高度

    #链接信号槽函数
    def signal_func(self):
        self.ui.pushButton.clicked.connect(self.Print) #启动按钮单击显示图片

    def Print(self):

        for i in range(len(self.data)):
            x = self.end_dot_list[-1][0]+self.x_num1
            y = self.data[i]*self.y_num1
            self.end_dot_list.append([x, y])

        self.picture.fill(Qt.white)  # 设置为白底色
        for end_dot_list in self.end_dot_list:
            self.end_x = end_dot_list[0]  # X轴终点位置
            self.end_y = 451 - end_dot_list[1] - 20
            self.update_show()
            self.ui.show_read.setPixmap(self.picture)  # 将图像显示在标签上

    def update_show(self):
        self.draw.begin(self.picture) # 开始在目标设备上绘制图像
        self.draw.setPen(QPen(QColor("black"), 2))  # 设置画笔颜色，粗细
        # 绘制一条指定了端点坐标的线，绘制从（self.beg_x,self.beg_y）到（self.end_x,self.end_y）的直线
        self.draw.drawLine(QPoint(self.beg_x, self.beg_y),QPoint(self.end_x, self.end_y) )
        self.draw.end() #结束在目标设备上面绘制
        self.beg_x = self.end_x #改变结束后的坐标
        self.beg_y = self.end_y

    def load_data(self):
        import numpy as np
        data = np.loadtxt('Cs137_1.txt')
        return data


if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())