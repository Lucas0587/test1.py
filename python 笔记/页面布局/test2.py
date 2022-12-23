import sys
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QCheckBox, QSpinBox, QHBoxLayout, \
    QComboBox, QGridLayout

class SignalEmit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print(1)
        self.creatContorls("打印控制：")

        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        self.setLayout(layout)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('defined signal')
        self.show()

    def creatContorls(self, title):
        self.controlsGroup = QGroupBox(title)
        self.printButton = QPushButton("打印")
        self.previewButton = QPushButton("预览")
        numberLabel = QLabel("打印份数：")
        pageLabel = QLabel("纸张类型：")
        self.previewStatus = QCheckBox("全屏预览")
        self.numberSpinBox = QSpinBox()
        self.numberSpinBox.setRange(1, 100)
        self.styleCombo = QComboBox(self)
        self.styleCombo.addItem("A4")
        self.styleCombo.addItem("A5")

        controlsLayout = QGridLayout()
        controlsLayout.addWidget(numberLabel, 0, 0)
        controlsLayout.addWidget(self.numberSpinBox, 0, 1)
        controlsLayout.addWidget(pageLabel, 0, 2)
        controlsLayout.addWidget(self.styleCombo, 0, 3)
        controlsLayout.addWidget(self.printButton, 0, 4)
        controlsLayout.addWidget(self.previewStatus, 3, 0)
        controlsLayout.addWidget(self.previewButton, 3, 1)
        self.controlsGroup.setLayout(controlsLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dispatch = SignalEmit()
    sys.exit(app.exec_())