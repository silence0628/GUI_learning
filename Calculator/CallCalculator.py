#coding:utf-8
"""

"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Calculator import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


    def addfunction(self):  ##用来实现加法的函数
        a = float(self.textEdit.toPlainText())
        b = float(self.textEdit2.toPlainText())
        c = a + b
        self.textEdit3.setText(str(c))
        self.textBrowser.append("%.2f + %.2f = %.2f" % (a, b, c))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())