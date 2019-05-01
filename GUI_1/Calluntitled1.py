# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def readModel(self):
        print('* start reading model!')
        modelName = self.ui.modelComboBox.currentText()
        model = self.transModelName(modelName)
        self.ui.resultText.setText(model)


    def transModelName(self, modelName):
        modelPath = ''
        if modelName == 'svd+svm':
            modelPath = '../log/log1/'
        elif modelName == '一维卷积神经网络':
            modelPath = '../log/log2/'
        elif modelName == '二维卷积神经网络':
            modelPath = '../log/log3/'

        return modelPath

if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())