import threading
import socket
import time
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui

PORT = 9998

s_client = socket.socket()
s_server = socket.socket()

CNT = False
LIS = False
REQ = ''

c_server_client = ''


def client(self, HOST):
    global s_client
    global CNT
    global LIS
    global REQ

    LIS = True
    REQ = HOST
    s_client.connect((HOST, PORT))
    data = s_client.recv(1024).decode()

    if data == 'ALLOW':
        CNT = True
    else:
        LIS = False
        s_client.close()
        s_client = socket.socket()
        QtWidgets.QMessageBox.information(self, '연결 요청 실패', f"연결 요청이 거부되었습니다.")


def server(self):
    global c_server_client
    global CNT
    global s_server

    while (True):
        while (True):
            s_server.bind(("", PORT))
            s_server.listen()

            c_server_client, ad = s_server.accept()
            ip = list(ad)[0]

            if ip != REQ:
                ans = QtWidgets.QMessageBox.information(self, '연결 요청 감지', f"{ip}로부터 연결이 요청되었습니다.",
                                                        QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                if ans == QtWidgets.QMessageBox.Yes:
                    if not LIS:
                        s_client.connect((ip, PORT))
                        c_server_client.sendall('ALLOW'.encode())
                        break
                else:
                    c_server_client.sendall('DENY'.encode())
                    s_server = socket.socket()
            else:
                c_server_client.sendall('ALLOW'.encode())
                break

        CNT = True
        uid = list(ad)[0].split(".")[3]

        while (CNT):
            data = c_server_client.recv(1024)
            ms = data.decode()
            self.console.append(f'유저{uid}: {ms}')

        CNT = False
        c_server_client.close()
        s_server.close()
        s_server = socket.socket()


class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 350, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("GUI.svg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.button_connect = QtWidgets.QPushButton(self.centralwidget)
        self.button_connect.setGeometry(QtCore.QRect(45, 70, 45, 25))
        self.button_connect.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.button_connect.setText("")
        self.button_connect.setObjectName("button_connect")
        self.button_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.button_minimize.setGeometry(QtCore.QRect(280, 2, 31, 31))
        self.button_minimize.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.button_minimize.setText("")
        self.button_minimize.setObjectName("button_minimize")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(269, 448, 60, 40))
        self.button_send.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.button_send.setText("")
        self.button_send.setObjectName("button_send")
        self.button_quit = QtWidgets.QPushButton(self.centralwidget)
        self.button_quit.setGeometry(QtCore.QRect(100, 70, 45, 25))
        self.button_quit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.button_quit.setText("")
        self.button_quit.setObjectName("button_quit")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(320, 0, 31, 31))
        self.button_exit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.button_exit.setText("")
        self.button_exit.setObjectName("button_exit")
        self.text_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.text_ip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_ip.setGeometry(QtCore.QRect(25, 39, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.text_ip.setFont(font)
        self.text_ip.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.text_ip.setObjectName("text_ip")
        self.text_ms = QtWidgets.QTextEdit(self.centralwidget)
        self.text_ms.setGeometry(QtCore.QRect(36, 448, 200, 40))
        # font = QtGui.QFont()
        # font.setFamily("Agency FB")
        # font.setPointSize(9)
        # font.setBold(True)
        # font.setWeight(75)
        self.text_ms.setFont(font)
        self.text_ms.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.text_ms.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_ms.setObjectName("text_ms")
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(30, 130, 291, 291))
        # font = QtGui.QFont()
        # font.setFamily("Agency FB")
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        # self.console.setFont(font)
        self.console.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.console.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console.setReadOnly(True)
        self.console.setObjectName("console")
        self.myconsole = QtWidgets.QLineEdit(self.centralwidget)
        self.myconsole.setGeometry(QtCore.QRect(30, 130, 291, 291))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.myconsole.setFont(font)
        self.myconsole.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.myconsole.setFrame(False)
        self.myconsole.setReadOnly(True)
        self.myconsole.setObjectName("myconsole")
        self.check_rsa = QtWidgets.QCheckBox(self.centralwidget)
        self.check_rsa.setGeometry(QtCore.QRect(301, 47, 21, 16))
        self.check_rsa.setText("")
        self.check_rsa.setChecked(True)
        self.check_rsa.setTristate(False)
        self.check_rsa.setObjectName("check_rsa")
        self.check_text = QtWidgets.QCheckBox(self.centralwidget)
        self.check_text.setGeometry(QtCore.QRect(301, 75, 21, 16))
        self.check_text.setText("")
        self.check_text.setObjectName("check_text")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_connect.clicked.connect(self.start_connect)
        self.button_send.clicked.connect(self.send_ms)
        self.button_quit.clicked.connect(self.quit)

        self.button_minimize.clicked.connect(self.minimize)
        self.button_exit.clicked.connect(self.exit)

        self.button_connect.setStyleSheet(
            '''
            QPushButton{background-color: rgba(39, 39, 39, 0);}
            QPushButton:hover{background-color: rgba(39, 39, 39, 100);}
            '''
        )

        self.button_send.setStyleSheet(
            '''
            QPushButton{background-color: rgba(39, 39, 39, 0);}
            QPushButton:hover{background-color: rgba(39, 39, 39, 100);}
            '''
        )

        self.button_quit.setStyleSheet(
            '''
            QPushButton{background-color: rgba(39, 39, 39, 0);}
            QPushButton:hover{background-color: rgba(39, 39, 39, 100);}
            '''
        )

        self.button_minimize.setStyleSheet(
            '''
            QPushButton{background-color: rgba(39, 39, 39, 0);}
            QPushButton:hover{background-color: rgba(39, 39, 39, 100);}
            '''
        )

        self.button_exit.setStyleSheet(
            '''
            QPushButton{background-color: rgba(39, 39, 39, 0);}
            QPushButton:hover{background-color: rgba(39, 39, 39, 100);}
            '''
        )

        s_thread = threading.Thread(target=server, args=(self,))
        s_thread.daemon = True
        s_thread.start()

    def center(self):
        qr = self.frameGeometry()
        cp = QtCore.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def minimize(self):
        self.showMinimized()

    def exit(self):
        sys.exit(app.exec_())

    def start_connect(self):
        if not CNT:
            c_ip = self.text_ip.toPlainText()
            print(c_ip)

            c_thread = threading.Thread(target=client, args=(self, c_ip))
            c_thread.daemon = True
            c_thread.start()
        else:
            print('이미 연결상태 입니다.')

    def quit(self):
        global CNT
        global s_client

        if CNT:
            CNT = False
            time.sleep(0.5)
            s_client.close()
            s_client = socket.socket()
        else:
            print('연결 상태가 아닙니다.')

    def send_ms(self):
        if CNT:
            ms = self.text_ms.toPlainText()
            s_client.sendall(ms.encode())
            if not ms == "":
                self.console.append(f'나: {ms}')
            self.text_ms.setText("")
        else:
            print('연결이 되지 않았습니다.')

    def deny_alret(self):
        QtWidgets.QMessageBox.information(self, '연결 요청 실패', f"연결 요청이 거부되었습니다.")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    myWindow.show()
    sys.exit(app.exec_())
    s_client.close()
    s_server.close()
    c_server_client.close()

    # QObject::setParent: Cannot set parent, new parent is in a different thread
