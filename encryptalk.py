import threading
import socket
import time
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

PORT = 9999

s_client = socket.socket()
s_server = socket.socket()

CNT = False
CCN = False
SCN = False


c_server_client = ''

def client(HOST):
    global s_client
    global CCN

    s_client.connect((HOST,PORT))
    print('클라이언트 연결 성공')
    CCN = True
    while(not(SCN)):
        time.sleep(1.5)
        print('클라이언트 연결 대기중')


def server(self):
    global c_server_client
    global SCN
    global CNT

    s_server.listen()

    s_server.bind(("", PORT))
    c_server_client, ad = s_server.accept()
    print('서버 연결 성공')
    SCN = True
    while(not(CCN)):
        time.sleep(1.5)
        print('클라이언트 연결 대기중')
    CNT = True


    while(True):
        data = c_server_client.recv(1024)
        ms = data.decode()
        self.console.append(f'유저{ad}: {ms}\n')
        if ms == '종료':
            break

    c_server_client.close()


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

        self.pushButton.clicked.connect(self.start_connect)
        self.button_send.clicked.connect(self.send_ms)

    def start_connect(self):
        global CNT

        c_ip = self.text_ip.toPlainText()

        c_thread = threading.Thread(target=client,args=(c_ip,))
        s_thread = threading.Thread(target=server,args=(self,))

        c_thread.daemon = True
        s_thread.daemon = True

        c_thread.start()
        s_thread.start()

    def send_ms(self):
        if CNT:
            ms = self.text_ms.toPlainText()
            s_client.sendall(ms.encode())
        else:
            print('연결이 되지 않았습니다.')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
    s_client.close()
    s_server.close()
