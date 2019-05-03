# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hhh.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 790, 127, 34))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.show_read = QtWidgets.QLabel(self.centralwidget)
        self.show_read.setGeometry(QtCore.QRect(10, 0, 981, 451))
        self.show_read.setStyleSheet("background-color: rgb(245, 250, 246);")
        self.show_read.setObjectName("show_read")

        self.show_read_2 = QtWidgets.QLabel(self.centralwidget)
        self.show_read_2.setGeometry(QtCore.QRect(350, 460, 320, 320))
        self.show_read_2.setStyleSheet("background-color: rgb(245, 250, 246);")
        self.show_read_2.setObjectName("show_read_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 28))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "核素识别系统"))
        self.pushButton.setText(_translate("MainWindow", "打印输出"))
        self.show_read.setText(_translate("MainWindow", "一维信号显示图"))
        self.show_read_2.setText(_translate("MainWindow", "二维图像显示图"))


