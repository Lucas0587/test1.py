import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QWidget
def click():
    print("Hy Button is clicked!")
app = QApplication(sys.argv)    #每个GUI都必须包含一个Qapplication，argv表示获取命令行参数，如果不用获取，则可以使用[]代替。
win = QMainWindow()

win.setGeometry(300, 300, 960, 640)
win.setWindowTitle("Pyqt5 Tutorial")

button = QPushButton(win)
button.resize(192, 108)     #resize:组件大小
button.setText("Hi! Click Me")
button.move(100, 100)
button.clicked.connect(click)

label=QLabel(win)
label.resize(500, 500)
label.setText("Hi this is Pyqt5")
label.move(100, 100)



win.show()

sys.exit(app.exec_())