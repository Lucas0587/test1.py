import sys,random,xlrd,os
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtWidgets import *

'''------------开始页面------------'''
page = QApplication(sys.argv)

class parent_page:
    def quit(self):
        exit()

    def choose(self):
        file=QFileDialog.getOpenFileNames(None,'选择文件',os.getcwd(), "All Files(*);;Text Files(*.txt)")
        fpath=str(file[0]).replace('/','\\').replace('\'',' ').replace('[',' ').replace(']',' ').strip()        #获取文件路径
        fname=os.path.basename(fpath)      #获取文件名
        if ".xlsx" not in fname:
            QMessageBox.warning(self.win_start,"警告","选择的不是excel文件")
        else:
            self.label_tip4.setText(fpath)

    def __init__(self):
        self.win_start = QMainWindow()
        self.win_start.setFixedSize(640, 360)
        self.win_start.move(300, 300)
        self.win_start.setWindowTitle("Slide_Start")
        self.win_start.setObjectName("MainWindow")
        self.win_start.setStyleSheet("#MainWindow{background-color:#F7FED5;}")

        self.label_tip = QLabel(self.win_start)
        self.label_tip.resize(600,50)
        self.label_tip.setText("Slide自查器")
        self.label_tip.setAlignment(Qt.AlignCenter)
        self.label_tip.setStyleSheet("QLabel{background-color:#94d2ef;font-size:30px}")

        self.label_tip1 = QLabel(self.win_start)
        self.label_tip1.resize(400,40)
        self.label_tip1.setText("请在右侧选择需要的功能，然后点击确认")
        self.label_tip1.setAlignment(Qt.AlignCenter)
        self.label_tip1.setStyleSheet("QLabel{font-size:18px}")

        information=["问题猜答案","答案猜问题"]
        self.combox=QComboBox(self.win_start)
        self.combox.addItems(information)
        self.combox.resize(180,40)

        self.label_tip2=QLabel(self.win_start)
        self.label_tip2.resize( 400, 40)
        self.label_tip2.setText("请选择需要使用的文档，\n若不选择则默认选择最近打开的文档")
        self.label_tip2.setAlignment(Qt.AlignCenter)
        self.label_tip2.setStyleSheet("QLabel{font-size:18px}")

        self.button_choose = QPushButton(self.win_start)
        self.button_choose.setText("选择")
        self.button_choose.resize(180,40)
        self.button_choose.clicked.connect(self.choose)

        self.label_tip3 = QLabel(self.win_start)
        self.label_tip3.resize(110, 40)
        self.label_tip3.setText("文件路径为：")
        self.label_tip3.setStyleSheet("QLabel{font-size:18px}")

        self.label_tip4 = QLabel(self.win_start)
        self.label_tip4.resize(490, 40)
        self.label_tip4.setText("")
        self.label_tip4.setContentsMargins(15,5,5,5)
        self.label_tip4.setStyleSheet("QLabel{font-size:18px}")

        self.button_start=QPushButton(self.win_start)
        self.button_start.setText("开始")
        self.button_exit = QPushButton(self.win_start)
        self.button_exit.setText("退出")
        self.button_exit.clicked.connect(self.quit)


        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()  # 水平布局管理器
        self.v_layout = QVBoxLayout()
        self.layout_init()

        self.win_start.show()
        sys.exit(page.exec())

    def layout_init(self):
        #水平布局管理器1
        self.h1_layout.addWidget(self.label_tip1)
        self.h1_layout.addWidget(self.combox)
        #水平布局管理器2
        self.h2_layout.addWidget(self.label_tip1)
        self.h2_layout.addWidget(self.button_choose)
        #水平布局管理器3
        self.h3_layout.addWidget(self.button_start)
        self.h3_layout.addWidget(self.button_exit)
        #垂直布局管理器
        self.v_layout.addWidget(self.label_tip)
        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addLayout(self.h3_layout)
        #设置最终布局
        self.win_start.setLayout(self.v_layout)

def main():
    sheetbook = xlrd.open_workbook("slide.xlsx")  # 打开表格
    sheet0 = sheetbook.sheets()[0]  # 找到第一个表格
    nrows = sheet0.nrows  # 获取给定表格数据的总行数
    parent_page()

if __name__ == '__main__':
    main()