import threading
import socket
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

HOST = '203.253.198.247'
PORT = 9999

def client():
    s = socket.socket()

    s.connect((HOST,PORT))

    while(True):
        ms = input('문자: ')
        s.sendall(ms.encode())
        print(f'나: {ms}\n')
        if ms == '종료':
            break

    s.close()

def server():
    s = socket.socket()

    s.bind(("", PORT))
    s.listen()

    cs, ad = s.accept()

    while(True):
        data = cs.recv(1024)
        ms = data.decode()
        print(f'유저{ad.split(".")[3]}: {ms}\n')
        if ms == '종료':
            break

    s.close()


class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(340, 470)
        MainWindow.setMinimumSize(QtCore.QSize(340, 470))
        MainWindow.setMaximumSize(QtCore.QSize(340, 470))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_ms = QtWidgets.QTextEdit(self.centralwidget)
        self.text_ms.setGeometry(QtCore.QRect(10, 350, 241, 71))
        self.text_ms.setObjectName("text_ms")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(260, 350, 71, 71))
        self.button_send.setObjectName("button_send")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 10, 51, 31))
        self.pushButton.setObjectName("pushButton")
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(10, 60, 321, 281))
        self.console.setReadOnly(True)
        self.console.setObjectName("console")
        self.text_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.text_ip.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.text_ip.setObjectName("text_ip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "채팅"))
        self.button_send.setText(_translate("MainWindow", "보내기"))
        self.pushButton.setText(_translate("MainWindow", "연결"))

class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
