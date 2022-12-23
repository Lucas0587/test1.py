'''import sys
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QCheckBox, QSpinBox, QHBoxLayout, \
    QComboBox, QGridLayout,QMainWindow

class Test():
    def __init__(self):
        super().__init__()
        self.win=QMainWindow()
        self.button_long_add = QPushButton(self.win)
        self.button_long_del = QPushButton(self.win)
        self.button_long_ope = QPushButton(self.win)
        self.controlsGroup()

        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        self.win.setLayout(layout)

        self.win.show()

    def controlsGroup(self):
        controlsLayout = QGridLayout()
        controlsLayout.addWidget(self.button_long_add,0,0)
        controlsLayout.addWidget(self.button_long_ope,0,1)
        controlsLayout.addWidget(self.button_long_del,1,1)
        self.controlsGroup.setLayout(controlsLayout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dispatch = Test()
    sys.exit(app.exec_())'''
from PyQt5.QtWidgets import *
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        button = QPushButton("弹出子窗", self)
        button.clicked.connect(self.show_child)

    def show_child(self):
        self.child_window = Child()
        self.child_window.show()


class Child(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是子窗口啊")


# 运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())