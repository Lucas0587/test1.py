import sys,random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon

class page_random(QMainWindow):
    def __init__(self):
        super(page_random, self).__init__()
        self.win_xuanze=QMainWindow()
        self.label_explain=QLabel(self.win_xuanze)
        self.label_num=QLabel(self.win_xuanze)
        self.button_choose=QPushButton(self.win_xuanze)
        self.layout_init()

    def random_num(self):
        randomnum=random.randint(1,10)
        self.label_num.setStyleSheet("QLabel{background-color: #000000}")
        self.label_num.setStyleSheet("QLabel{background-color: #ffffff;font-size:25px;}")
        self.label_num.setText(str(randomnum))

    def layout_init(self):
        self.win_xuanze.setFixedSize(960, 540)
        self.win_xuanze.move(300, 300)
        self.win_xuanze.setWindowTitle("随机数生成器")  # 设置界面

        self.label_explain.setText("点击按钮随机生成一个随机数")
        self.label_explain.move(40,40)
        self.label_explain.resize(300,40)
        self.label_explain.setAlignment(Qt.AlignRight)
        self.label_explain.setContentsMargins(15, 5, 15, 5)
        self.label_explain.setStyleSheet("QLabel{font-size:18px;}")

        self.label_num.move(500, 40)
        self.label_num.resize(100, 40)
        self.label_num.setAlignment(Qt.AlignCenter)
        self.label_num.setStyleSheet("QLabel{background-color: #ffffff;font-size:25px;}")

        self.button_choose.setText("选择")
        self.button_choose.move(360,40)
        self.button_choose.resize(120,40)
        self.button_choose.clicked.connect(self.random_num)



def index():
    page = QApplication(sys.argv)
    win = page_random()
    win.win_xuanze.show()
    sys.exit(page.exec())

if __name__ == '__main__':
    index()