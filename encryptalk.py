import threading
import socket
import time
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

PORT = 9999

s_client = socket.socket()
s_server = socket.socket()

CNT = False
LIS = False
REQ = ''

c_server_client = ''

def client(self,HOST):
    global s_client
    global CNT
    global LIS
    global REQ

    LIS = True
    REQ = HOST
    s_client.connect((HOST,PORT))
    data = s_client.recv(1024).decode()

    if data == 'ALLOW':
        CNT = True
    else:
        LIS = False
        s_client.close()
        s_client = socket.socket()
        self.deny_alret()



def server(self):
    global c_server_client
    global CNT
    global s_server

    while(True):
        while(True):
                s_server.bind(("", PORT))
                s_server.listen()

                c_server_client, ad = s_server.accept()
                ip = list(ad)[0]

                if ip != REQ:
                    ans = self.connect_alret(ip)
                    if ans:
                        if not LIS:
                            s_client.connect((HOST, PORT))
                            c_server_client.sendall('ALLOW'.encode())
                            break
                    else:
                        c_server_client.sendall('DENY'.encode())
                        s_server.close()
                        s_server = socket.socket()
                else:
                    c_server_client.sendall('ALLOW'.encode())
                    break

        CNT = True
        uid = list(ad)[0].split(".")[3]

        while(True):
            data = c_server_client.recv(1024)
            ms = data.decode()
            self.console.append(f'유저{uid}: {ms}')

        CNT = False

        s_server.close()


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

        s_thread = threading.Thread(target=server,args=(self,))
        s_thread.daemon = True
        s_thread.start()


    def start_connect(self):
        global CNT

        if not CNT:
            c_ip = self.text_ip.toPlainText()

            c_thread = threading.Thread(target=client,args=(self,c_ip))
            c_thread.daemon = True
            c_thread.start()
        else:
            print('이미 연결상태 입니다.')

    def send_ms(self):
        if CNT:
            ms = self.text_ms.toPlainText()
            s_client.sendall(ms.encode())
            if not ms == "":
                self.console.append(f'나: {ms}')
            self.text_ms.setText("")
        else:
            print('연결이 되지 않았습니다.')

    def connect_alret(self,ip):
        buttonReply = QtWidgets.QMessageBox.information(self, '연결 요청 감지', f"{ip}로부터 연결이 요청되었습니다.", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if buttonReply == QtWidgets.QMessageBox.Yes:
            return True
        elif buttonReply == QtWidgets.QMessageBox.No:
            return False

    def deny_alret(self):
        QtWidgets.QMessageBox.information(self, '연결 요청 실패', f"연결 요청이 거부되었습니다.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
    s_client.close()
    s_server.close()
    c_server_client.close()
