# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from untitled2 import Ui_MainWindow
import requests
import os
from PIL import Image
import numpy as np


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.draw = QPainter()
        self.path = './data/'
        self.url = './data/Cs137_1.txt'
        self.k = 0
        self.signal_func() # 初始化信号槽函数，

        self.data = np.array('d')

    #链接信号槽函数
    def signal_func(self):
        self.ui.startButton.clicked.connect(self.Print) #启动按钮单击显示图片
        # self.ui.endButton.clicked.connect(self.clear)  #停止按钮单击信号

    idx = 0
    N = 200
    def Print(self):
        print('* start reading model!')


        # **********读取图片***********************************************
        # modelName = self.ui.modelComboBox.currentText()
        #
        # if self.k >= 0 and self.k <=3:
        #     self.k = self.k + 1
        # else:
        #     self.k = self.k
        # model= self.transModelName(modelName, self.k)
        # self.ui.resultText.setText(model)  # 发送文字到label显示
        # self.ui.resultText.setPixmap(QtGui.QPixmap(url)) #在label上显示图片

        # **********读取txt***********************************************
        # f = open(self.url)
        # text = f.read()
        # # self.ui.resultText.setText(text)  # 发送文字到label显示
        # self.draw.begin(self.ui.resultText)  # 开始在目标设备上面绘制
        # self.draw.drawLine(text)





    # def downPrint(self):
    #     modelName = self.ui.modelComboBox.currentText()
    #     if self.k >= 1 and self.k <=4:
    #         self.k = self.k - 1
    #     else:
    #         self.k = self.k
    #     model, url = self.transModelName(modelName, self.k)
    #     # self.ui.resultText.setText(model)  # 发送文字到label显示
    #     self.ui.resultText.setPixmap(QtGui.QPixmap(url)) #在label上显示图片


    def transModelName(self, modelName, k):
        modelPath = ''

        imgLists = os.listdir(self.path)

        if modelName == 'SVD+SVM':
            modelPath = '../log/log1/'
            # url = self.path +'/'+ imgLists[k]
        elif modelName == '一维卷积神经网络':
            modelPath = '../log/log2/'
            # url = self.path +'/'+ imgLists[k]
        elif modelName == '二维卷积神经网络':
            modelPath = '../log/log3/'
            # url = self.path +'/'+ imgLists[k]

        return modelPath

    # def selectPath(self):
    #     self.path = QFileDialog.getExistingDirectory(self,
    #                                 "打开文件夹") # 起始路径
    #
    #     print(self.path)




if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())