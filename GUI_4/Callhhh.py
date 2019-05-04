# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from hhh2 import Ui_MainWindow
import requests
import os
from PIL import Image
import numpy as np
import numpy as np
import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QFrame,QGridLayout,QLabel,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt,QTimer

# 导入核素识别模型
# from Nuclide_CNN import main
# from Nuclide_CNN import model
# from Nuclide_CNN import utils


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
        self.picture = QPixmap(711, 171)  # 设置图片大小

        self.end_dot_list = [[0, 0]]  # 保存绘制点位列表
        self.beg_x = 0
        self.beg_y = 0

        self.x_num = 4096 #X轴分成多少等份
        self.y_num = 1000 #Y轴分成多少等份

        self.x_num1 = 711/self.x_num #每一等份的宽度
        self.y_num1 = 171/self.y_num #每一等份的高度

        self.img_path = './tmp/tmp.jpg' # 加载数据二维图像路径
        self.txt_path = './txts/Cs137_1.txt' # 加载一维数据路径
        self.cwd = './txts/'


    #链接信号槽函数
    def signal_func(self):
        self.ui.pushButton.clicked.connect(self.plot_spectrum) #启动按钮单击显示图片
        self.ui.pushButton.clicked.connect(self.load_img)  # 启动按钮单击显示图片
        self.ui.select_txt_Button.clicked.connect(self.select_txt)

    def plot_spectrum(self):

        self.data = self.load_data()

        for i in range(len(self.data)):
            x = self.end_dot_list[-1][0]+self.x_num1
            y = self.data[i]*self.y_num1
            self.end_dot_list.append([x, y])

        self.picture.fill(Qt.white)  # 设置为白底色
        for end_dot_list in self.end_dot_list:
            self.end_x = end_dot_list[0]  # X轴终点位置
            self.end_y = 171 - end_dot_list[1] - 20
            self.update_show()
            self.ui.show_read.setPixmap(self.picture)  # 将图像显示在标签上

    def update_show(self):
        self.draw.begin(self.picture) # 开始在目标设备上绘制图像
        self.draw.setPen(QPen(QColor("black"), 2))  # 设置画笔颜色，粗细
        # 绘制一条指定了端点坐标的线，绘制从（self.beg_x,self.beg_y）到（self.end_x,self.end_y）的直线
        self.draw.drawLine(QPoint(self.beg_x, self.beg_y),QPoint(self.end_x, self.end_y))
        self.draw.end() #结束在目标设备上面绘制
        self.beg_x = self.end_x #改变结束后的坐标
        self.beg_y = self.end_y

    def load_data(self):
        import numpy as np
        data = np.loadtxt(self.txt_path)
        return data

    def load_img(self):
        from PIL import Image

        import numpy as np

        data = np.loadtxt(self.txt_path)
        data = data.reshape(64, 64)
        # data = np.resize(data, (150, 150))

        import scipy.misc
        scipy.misc.imsave(self.img_path, data)
        self.ui.show_read_2.setPixmap(QtGui.QPixmap(self.img_path))  # 在label上显示图片

    # 更改模型选择，
    def transModelName(self, modelName, k):
        model_path = ''
        if modelName == 'SVD+SVM':
            model_path = '../Nuclide_CNN/log1/'

        elif modelName == '一维卷积神经网络':
            model_path = '../Nuclide_CNN/checkpoint_1D/'

        elif modelName == '二维卷积神经网络':
            model_path = '../Nuclide_CNN/checkpoint/'

        return model_path

    def select_txt(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "选取文件",
                                                                self.cwd,         #起始路径
                                                                "All Files (*);;Text Files (*.txt)") # 设置文件扩展名过滤,用双分号间隔

        self.txt_path = fileName_choose
        self.ui.show_read.clear()
        self.ui.show_read_2.clear()



if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())