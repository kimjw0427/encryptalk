
import threading
import socket
import time
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui
import tkinter as tk
from tkinter import messagebox

import random

ML_A = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999]

S_D = 0
S_N = 0

C_E = 0
C_N = 0

def Q_mod(x, d, n):
    y = x % n
    r = 1
    bd = bin(d)
    bd = bd[2:len(bd)]
    m = len(bd) - 1
    while (m != -1):
        if bd[m] == '1':
            r = r * y % n
        y = y ** 2 % n
        m = m - 1
    return r


def ML_test(n, a):
    d = (n - 1) // 2
    while (d % 2 == 0):
        if (pow(a, d, n) == n - 1):
            return True
        d = d // 2
    tmp = pow(a, d, n)
    if tmp == n - 1 or tmp == 1:
        return True
    else:
        return False


def F_test(n):
    a = 3
    if Q_mod(a, n - 1, n) == 1 or n == 3:
        return True
    else:
        return False


def prime_test(n):
    result = True
    if F_test(n):
        for x in ML_A:
            if not ML_test(n, x):
                result = False
                break
            if result:
                return True
    else:
        return False


def extended_euclid(r1, r2, s1=1, s2=0, t1=0, t2=1):
    # 처음 시작 시 s1 ~ t2 초기값 설정
    q = r1 // r2  # 두 수의 몫
    s = s1 - s2 * q  # 첫 번째 항의 곱
    t = t1 - t2 * q  # 두 번째 항의 곱
    r = r1 - r2 * q  # 두 수의 나머지와 같다.
    if (r == 0):
        res = {'gcd': r2, 's': s2, 't': t2}
        return res
    else:
        return extended_euclid(r2, r, s2, s, t2, t)


def find_d(e, Pn):
    res = extended_euclid(e, Pn)
    r = res['s']
    if r < 0:
        r = r + Pn
    return r


def gen_prime():
    N = random.randint(10 ** 127, 10 ** 128 - 1)
    while (not prime_test(N)):
        N = N + 1
    return N


def RSA():
    p = gen_prime()
    q = gen_prime()

    e = 65537

    Pn = (p - 1) * (q - 1)
    n = p * q

    d = find_d(e, Pn)

    return [e, d, n]


def encryption(a, e, n):
    return Q_mod(a, e, n)


def decryption(enc, d, n):
    return Q_mod(enc, d, n)

def enc_int(text):
    result = ''
    for i in range(0,len(text)):
        enc_code = str(ord(text[i]))
        if len(enc_code) <5:
            enc_code = '0'*(5-len(enc_code)) + enc_code
        result = result + enc_code
    result = '1' + result
    return int(result)

def dec_int(code):
    code = str(code)
    result = ''
    code = code[1:len(code)]
    for i in range(0,len(code),5):
        result = result + chr(int(code[i:i+5]))
    return result

def split_string(text):
    result = []
    if len(text) > 12:
        for i in range(0,len(text),12):
            result.append(text[i:i+12])
    else:
        return [text]
    return result

def trans_enc(text):
    text = split_string(text)
    result = ''
    for i in text:
        result = f'{result}/{encryption(enc_int(i),C_E,C_N)}'
    return result

def trans_dec(code):
    code = code.split('/')
    result = ''
    for i in range(1,len(code)):
        result = result + dec_int(decryption(int(code[i]),S_D,S_N))
    return result


PORT = 9997

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

    global C_E
    global C_N

    LIS = True
    REQ = HOST
    s_client.connect((HOST, PORT))
    data = s_client.recv(1024).decode()

    if data == 'ALLOW':
        CNT = True

        s_client.sendall('RD'.encode())
        C_E = int(s_client.recv(1024).decode())
        self.console.append(f'[클라이언트] 암호화 키 저장')

        s_client.sendall('RD2'.encode())
        C_N = int(s_client.recv(1024).decode())
        self.console.append(f'[클라이언트] 공개 키 저장')

        print('client complete')
        time.sleep(10)

    else:
        LIS = False
        s_client.close()
        s_client = socket.socket()
        root = tk.Tk()
        tk.messagebox.showinfo('연결 요청 실패','요청이 거부되었습니다.')
        root.destroy()


def server(self):
    global c_server_client
    global CNT
    global s_server

    global S_D
    global S_N
    global C_E
    global C_N

    while (True):
        while (True):
            s_server.bind(("", PORT))
            s_server.listen()

            c_server_client, ad = s_server.accept()
            ip = list(ad)[0]
            print('[',ip,']')

            if ip != REQ:
                root = tk.Tk()
                ans = tk.messagebox.askquestion('연결 요청 감지', f'{ip}로부터 연결 감지',icon='warning')
                root.destroy()
                if ans == 'yes':
                    if not LIS:
                        s_client.connect((ip, PORT))

                        c_server_client.sendall('ALLOW'.encode())

                        dummy = s_client.recv(1024)

                        s_client.sendall('RD'.encode())
                        C_E = int(s_client.recv(1024).decode())
                        self.console.append(f'[클라이언트] 암호화 키 저장')

                        s_client.sendall('RD2'.encode())
                        C_N = int(s_client.recv(1024).decode())
                        self.console.append(f'[클라이언트] 공개 키 저장')
                        print('client complete')
                        break
                else:
                    c_server_client.sendall('DENY'.encode())
                    s_server = socket.socket()
            else:
                c_server_client.sendall('ALLOW'.encode())
                break

        CNT = True

        key = RSA()
        S_D = key[0]
        S_N = key[2]

        if c_server_client.recv(1024).decode() == 'RD':
            c_server_client.sendall(str(key[1]).encode())
            self.console.append(f'[서버] 암호화 키 전송')
        else:
            self.console.append(f'[서버] 암호화 키 전송 에러!')
        if c_server_client.recv(1024).decode() == 'RD2':
            c_server_client.sendall(str(key[2]).encode())
            self.console.append(f'[서버] 공개 키 전송')
        else:
            self.console.append(f'[서버] 공개 키 전송 에러!')

        uid = list(ad)[0].split(".")[3]

        time.sleep(1)

        print(f'{S_N}\n{S_D}\n{C_N}\n{C_E}')

        print('Server complete')
        while (CNT):
            data = c_server_client.recv(1024)
            ms = data.decode()
            self.console.append(f'유저{uid}: {trans_dec(ms)}')

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
        self.background.setPixmap(QtGui.QPixmap("GUI_.png"))
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
            if ms != '':
                s_client.sendall(trans_enc(ms).encode())
                if not ms == "":
                    self.console.append(f'나: {ms}')
                self.text_ms.setText("")
        else:
            print('연결이 되지 않았습니다.')


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
