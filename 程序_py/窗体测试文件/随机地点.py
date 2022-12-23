import random
import sys
import time
from PyQt5.QtWidgets import *
from random import choices,sample
from PyQt5.QtCore import *
from PyQt5.QtGui import *
zist = ['1号线','2号线','3号线','4号线','5号线','6号线','7号线','8号线','9号线',
        '10号线','11号线','12号线','13号线','14号线','15号线','16号线','17号线','18号线','浦江线']
dic={"1号线":"#d41414","2号线":"#90c31f","3号线":"#fdd804","4号线":"#6241b8","5号线":"#bc54c0",
     "6号线":"#ba1b74","7号线":"#fe7800","8号线":"#1995d3","9号线":"#7ecef5","10号线":"#a989be",
     "11号线":"#7c0100","12号线":"#037c61","13号线":"#da6db1","14号线":"#8c864d","15号线":"b9a17b",
     "16号线":"#13b5b2","17号线":"#b37275","18号线":"#d1aa73","浦江线":"#9f9f9f"}
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(960,540)
        self.setWindowTitle('魔方抽奖')
        self.btn = QPushButton(self,text='抽奖')
        self.timer = QTimer()
        self.timer.timeout.connect(self.random_choose)
        self.btn.clicked.connect(lambda:self.timer.start(1))
        self.btn.resize(123,400)
        self.let = QLineEdit(self)
        self.let.setReadOnly(True)
        self.let.move(123,0)
        self.let.resize(400,400)
        self.let.setStyleSheet('QLineEdit{font-size:100px}')
        self.btn1 = QPushButton(self)
        self.btn1.setText('停止')
        self.btn1.clicked.connect(lambda:self.timer.stop())
    def random_choose(self):
        num=random.randint(1,19)
        name=dic.items()
        print(name)
        '''self.let.setText(''.join(dic.keys()))
        self.let.setAlignment(Qt.AlignCenter)
        self.let.setStyleSheet("")'''
        time.sleep(5)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Window()
    root.show()
    sys.exit(app.exec())
