import sys, os, slide, SingleChoose
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

'''------------开始页面------------'''


class index_page(QWidget):
    def __init__(self, parent=None):
        super(index_page, self).__init__(parent)
        self.win_start = QMainWindow()
        self.label_tip = QLabel(self.win_start)
        self.label_tip1 = QLabel(self.win_start)
        self.combox = QComboBox(self.win_start)
        self.label_tip2 = QLabel(self.win_start)
        self.button_choose = QPushButton(self.win_start)
        self.label_tip3 = QLabel(self.win_start)
        self.label_tip4 = QLabel(self.win_start)
        self.button_start = QPushButton(self.win_start)
        self.button_exit = QPushButton(self.win_start)
        self.label_tip5 = QLabel(self.win_start)
        self.layout_init()

    def informationtxt(self, fpath):
        pypath = os.getcwd()
        txt_path = pypath + "\\" + "information.txt"
        file = open(txt_path, 'w')
        file.write(fpath)
        file.close()

    def choose(self):
        file = QFileDialog.getOpenFileNames(None, '选择文件', os.getcwd(), "All Files(*);;Text Files(*.txt)")
        fpath = str(file[0]).replace('/', '\\').replace('\'', ' ').replace('[', ' ').replace(']', ' ').strip()  # 获取文件路径
        fname = os.path.basename(fpath)  # 获取文件名
        if ".xlsx" not in fname:
            QMessageBox.warning(self.win_start, "警告", "选择的不是excel文件")
        else:
            self.label_tip4.setText(fpath)
            self.informationtxt(fpath)

    def quit(self):
        if os.path.exists("information.txt"):
            os.remove("information.txt")
        exit()

    def start(self):
        text = self.combox.currentText()
        if text == "问题猜答案":
            self.index_ui = slide.child_page()
            self.index_ui.win_main.show()
            self.win_start.close()
        elif text == "单项选择":
            self.index_ui = SingleChoose.child_page_two()
            self.index_ui.win_xuanze.show()
            self.win_start.close()

    def layout_init(self):
        self.win_start.setFixedSize(640, 360)
        self.win_start.move(300, 300)
        self.win_start.setWindowTitle("主窗口")
        self.win_start.setObjectName("MainWindow")
        icon_path = os.getcwd()
        self.win_start.setWindowIcon(QIcon(icon_path + "\\icon\\" + "main.ico"))
        self.win_start.setStyleSheet("#MainWindow{background-color:#F7FED5;}")

        self.label_tip.move(20, 20)
        self.label_tip.resize(600, 50)
        self.label_tip.setText("Slide自查器")
        self.label_tip.setAlignment(Qt.AlignCenter)
        self.label_tip.setStyleSheet("QLabel{background-color:#94d2ef;font-size:30px}")

        self.label_tip1.move(20, 100)
        self.label_tip1.resize(400, 40)
        self.label_tip1.setText("请在右侧选择需要的功能")
        self.label_tip1.setAlignment(Qt.AlignCenter)
        self.label_tip1.setStyleSheet("QLabel{font-size:18px}")

        self.combox.move(430, 100)
        self.combox.resize(180, 40)
        information = ["问题猜答案", "单项选择"]
        self.combox.addItems(information)

        self.label_tip2.move(20, 150)
        self.label_tip2.resize(400, 40)
        self.label_tip2.setText("请选择需要使用的文档，\n若不选择则默认选择模板文档")
        self.label_tip2.setAlignment(Qt.AlignCenter)
        self.label_tip2.setStyleSheet("QLabel{font-size:18px}")

        self.button_choose.move(430, 150)
        self.button_choose.setText("选择")
        self.button_choose.resize(180, 40)
        self.button_choose.clicked.connect(self.choose)

        self.label_tip3.move(20, 220)
        self.label_tip3.resize(120, 40)
        self.label_tip3.setText("文件路径为：")
        self.label_tip3.setStyleSheet("QLabel{font-size:18px}")
        self.label_tip3.setAlignment(Qt.AlignCenter)

        self.label_tip4.move(140, 220)
        self.label_tip4.resize(490, 40)
        if os.path.exists("information.txt"):
            with open("information.txt", "r") as f:
                text_path = f.readline()
                self.label_tip4.setText(text_path)
        self.label_tip4.setContentsMargins(15, 5, 5, 5)
        self.label_tip4.setStyleSheet("QLabel{background-color:#ffffff;font-size:18px}")

        self.label_tip5.setGeometry(10, 320, 200, 30)
        self.label_tip5.setText("版本号：1.2.0")

        self.button_start.resize(120, 30)
        self.button_start.move(100, 280)
        self.button_start.setText("开始")
        self.button_start.clicked.connect(self.start)

        self.button_exit.resize(120, 30)
        self.button_exit.move(400, 280)
        self.button_exit.setText("退出")
        self.button_exit.clicked.connect(self.quit)


def main():
    page = QApplication(sys.argv)
    win = index_page()
    win.win_start.show()
    sys.exit(page.exec())


if __name__ == '__main__':
    main()