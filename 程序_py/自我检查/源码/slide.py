import sys,random,xlrd,os,main
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon

'''------------主页面------------'''
class child_page(QMainWindow):
    def __init__(self):
        super(child_page, self).__init__()
        self.win_main = QMainWindow()
        self.button_slide = QPushButton(self.win_main)
        self.button_check = QPushButton(self.win_main)
        self.button_clear = QPushButton(self.win_main)
        self.button_confirm = QPushButton(self.win_main)
        self.button_exittomain = QPushButton(self.win_main)
        #self.button_xuanzhe=QPushButton(self.win_main)
        self.label_explain = QLabel(self.win_main)
        self.label_word = QLabel(self.win_main)
        self.label_answer = QLabel(self.win_main)
        self.label_tip=QLabel(self.win_main)
        self.combox=QComboBox(self.win_main)
        self.layout_init()

    def confirm(self):
        text=int(self.combox.currentText().strip("px"))
        if self.label_word !="":
            self.label_answer.setFont(QFont("",text))
            self.label_answer.setStyleSheet("QLabel{background-color: #ffffff;}")  # 设置label样式
    def randomword(self):
        if os.path.exists("information.txt"):
            f=open("information.txt","r")
            fpath=f.read()
            f.close()
        else:
            dirpath=os.getcwd()
            fpath=dirpath+"\\"+"Templete.xlsx"
        #print(fpath)
        sheetbook = xlrd.open_workbook(fpath)  # 打开表格
        sheetname=sheetbook.sheet_names()       #获取名称
        sheetData=sheetbook.sheet_by_name(sheetname[0])     #
        num_rows = sheetData.nrows
        randomnum = random.randint(2, num_rows)  # 生成随机数
        text1 = sheetData.cell_value(randomnum - 1, 0)  # 获取文本
        text2 = sheetData.cell_value(randomnum - 1, 1)
        text3 = sheetData.cell_value(randomnum - 1, 2)
        self.label_word.setText(text1)  # label中展示文本
        self.label_answer.setText(text2+"\t \t [备注："+text3+"]")
        self.label_answer.setStyleSheet("QLabel{background-color: #000000;"
                                   "font-size:20px;font-weight:normal;}")  # 设置label样式
    def clear(self):
        self.label_word.setText("")
        self.label_answer.setText("")
        self.label_answer.setStyleSheet("QLabel{background-color: #000000;}")  # 设置label样式
    def check(self):
        self.label_answer.setStyleSheet("QLabel{background-color: #000000;"
                                      "font-size:30px;font-weight:normal;}")  # 设置label样式
    def exittomain(self):
        self.win_main.close()
        self.slide_ui=main.parent_page()
        self.slide_ui.win_start.show()
        '''if os.path.exists("information.txt"):
            os.remove("information.txt")'''
    def layout_init(self):
        self.win_main.setFixedSize(960, 540)
        self.win_main.move(300, 300)
        icon_path=os.getcwd()
        self.win_main.setWindowIcon(QIcon(icon_path+"\\icon\\"+"slide.ico"))
        self.win_main.setWindowTitle("Slide_main")  # 设置界面

        self.button_slide.setText("下一个")
        self.button_slide.clicked.connect(self.randomword)  # 跳转到执行函数randomword
        self.button_slide.move(70, 400)  #设置开始button

        self.button_check.setText("隐藏")
        self.button_check.clicked.connect(self.check)  # 跳转到执行函数see
        self.button_check.move(610, 400)  # 设置清除button

        self.button_clear.setText("清除")
        self.button_clear.clicked.connect(self.clear)  # 跳转到执行函数clear
        self.button_clear.move(430, 400)  # 此三行设置清除button

        self.button_confirm.setText("偷偷看答案")
        self.button_confirm.clicked.connect(self.confirm)  # 跳转到执行函数confirm
        self.button_confirm.move(250, 400)  # 设置确认button

        self.button_exittomain.setText("返回")
        self.button_exittomain.clicked.connect(self.exittomain)
        self.button_exittomain.move(790, 400)  # 此三行设置确认button

        self.label_explain.move(10, 10)
        self.label_explain.resize(940, 80)
        self.label_explain.setWordWrap(True)
        self.label_explain.setAlignment(Qt.AlignCenter)
        self.label_explain.setText("本程序是自我检查程序，点击开始随机抽取，点击偷偷看答案查看答案")
        self.label_explain.setStyleSheet("QLabel{font-size:20px;}")  # 设置label样式

        self.label_word.setGeometry(20, 125, 920, 80)
        self.label_word.setWordWrap(True)
        self.label_word.setAlignment(Qt.AlignCenter)
        self.label_word.setStyleSheet("QLabel{background-color: #ffffff;"
                                      "font-size:20px;font-weight:normal;}")  # 设置label样式

        self.label_answer.setGeometry(20, 250, 920, 80)
        self.label_answer.setWordWrap(True)
        self.label_answer.setAlignment(Qt.AlignCenter)
        self.label_answer.setStyleSheet("QLabel{background-color: #000000;"
                                        "font-size:30px;font-weight:normal;}")  # 设置label样式

        self.label_tip.setGeometry(10,500,200,30)
        self.label_tip.setAlignment(Qt.AlignCenter)
        self.label_tip.setText("更改答案字号（默认12px）：")

        self.combox.setGeometry(220,500,200,30)
        list_mode = ["12px","14px","15px","16px","17px","18px","20px","24px","28px","30px","32px"]
        self.combox.addItems(list_mode)

def index():
    page = QApplication(sys.argv)
    win = child_page()
    win.win_main.show()
    sys.exit(page.exec())

if __name__ == '__main__':
    index()