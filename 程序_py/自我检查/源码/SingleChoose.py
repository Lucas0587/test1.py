import sys,random,xlrd,os,main
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon

'''------------主页面------------'''
text2="a"
text3=""
rightnum=0
wrongnum=0
num_word=0
count=0
listword=[]

def setIndex(self):
    if os.path.exists("search.txt"):  # 初始化使search.txt为空
        os.remove("search.txt")
    dirpath = os.getcwd()  # 获取当前路径
    if os.path.exists("information.txt"):  # 如果存在information.txt，则读取information.txt文件里面储存的地址fpath
        with open("information.txt", "r") as f:
            fpath = f.read()
    else:  # 否则默认fpath为该文件夹下的slide.xlsx
        fpath = dirpath + "\\" + "Templete.xlsx"
    sheetbook = xlrd.open_workbook(fpath)  # 打开表格
    sheetname = sheetbook.sheet_names()  # 获取名称
    sheetData = sheetbook.sheet_by_name(sheetname[0])  # 获取表格内容
    num_rows = sheetData.nrows  # 获取表格列数，由于第一行非内容行，因此实际items会比num_rows少1
    for i in range(0,num_rows):
        listword.append([sheetData.cell_value(i,0),sheetData.cell_value(i,1),sheetData.cell_value(i,2)])
    print(listword)
    return listword

class child_page_two(QMainWindow):
    list_total = pyqtSignal(list)
    def __init__(self):
        super(child_page_two, self).__init__()
        self.win_xuanze = QMainWindow()
        self.button_slide = QPushButton(self.win_xuanze)
        self.button_exittomain= QPushButton(self.win_xuanze)
        self.button_A = QPushButton(self.win_xuanze)
        self.button_B = QPushButton(self.win_xuanze)
        self.button_C = QPushButton(self.win_xuanze)
        self.button_D = QPushButton(self.win_xuanze)
        self.label_explain = QLabel(self.win_xuanze)
        self.label_word = QLabel(self.win_xuanze)
        self.label_right=QLabel(self.win_xuanze)
        self.label_tip=QLabel(self.win_xuanze)
        self.combox=QComboBox(self.win_xuanze)
        self.label_tip_size=QLabel(self.win_xuanze)
        self.combox_size=QComboBox(self.win_xuanze)
        self.layout_init()
        listword = setIndex(self)

    def randomword(self):
        def numsolve():       #定义处理excel数据的函数
            '''初始化变量'''
            global text2,num_word,text3     #设为全局变量
            count=0     #初始化count=0
            list=[]     #初始化list[]

            '''查找功能'''
            def search(text1,num_rows):      #定义寻找词条的函数
                if not os.path.exists("search.txt"):    #创建search.txt文件，用于筛查
                    f = open("search.txt", "a+")
                    f.close()
                txt_path = dirpath + "\\" + "search.txt"        #serach.txt文件地址为txt_path
                with open(txt_path,"r+") as file:       #打开文件
                    content=file.readlines()        #按行读取search.txt文件内容
                    for i in range(len(content)):       #在所读取到的内容中，如果存在text1（之前出现过该内容）则累加count
                        if text1==content[i].strip("\n"):
                            global count
                            count=count+1       #累加功能
                            file.close()        #关闭search.txt文件
                            if num_rows==count-1:     #如果累加结果等于列数，即所有的内容都读取完毕，那么弹出提示框并清除文件
                                self.message = QMessageBox(self.win_xuanze)
                                self.message.information(self.win_xuanze, "提示", "总共有{0}条目已全部展示，点击确认重新开始".format(num_rows-1))
                                try:
                                    os.remove("search.txt")
                                except:
                                    print("清除文件错误")
                                    exit()
                            return 1        #返回1继续查找
                    count=0     #查找结束后记得归零，否则下次查找会用上次查找结束的count值开始计数
                    file.write(text1+"\n")      #未跳出if，说明该内容并不是重复的内容，写入search.txt
                return 0    #返回0

            if self.combox.currentText()=="不重复出题":      #识别 “不重复出题” 模式，如果是 “重复出题” 模式则跳过此步
                num_word = num_word + 1     #开始计数不重复出题模式下共有多少词
                '''if num_word==num_rows+2:
                    self.message0=QMessageBox(self.win_xuanze)
                    self.message0.information(self.win_xuanze,"提示","共有{0}条目，已全部展示，点击确认重新开始".format(num_rows-1))
                    count=0
                    #self.exittomain(self)
                    try:
                        os.remove("search.txt")
                    except:
                        print("清除文件错误")
                        exit()'''
                Flag=search(text1,num_rows)      #寻找文本是否在serach.txt中
                while Flag==1:     #如果文本确实在search.txt中，重新生成text1并寻找
                        randomnum = random.randint(2, num_rows)  # 生成随机数
                        text1 = sheetData.cell_value(randomnum - 1, 0)  # 获取文本
                        Flag = search(text1,num_rows)
            text2= sheetData.cell_value(randomnum - 1, 1)       #text2为答案
            text3=sheetData.cell_value(randomnum-1,2)       #text3为备注
            countdata = 0       #初始化用于计数的countdata
            for i in range(2,num_rows):     #生成list[]
                if countdata==0:    #如果是第一个内容直接存入list[]
                    list.append(sheetData.cell_value(i,1))
                    countdata=countdata+1
                elif str(sheetData.cell_value(i,1))==str(list[count-1]):        #如果txt中已经有某item则跳过去
                    continue
                else:       #存入txt中没有的item
                    list.append(sheetData.cell_value(i, 1))
                    countdata=countdata+1
            self.label_word.setText(text1)      # label_word中展示文本text1
            return list     #返回list[]，下面要用
        def producechoose(list):        #生成四个选项
            textA=list[random.randint(0,len(list)-1)]                #生成A选项
            textB=list[random.randint(0, len(list) - 1)]
            while textB==textA:
                textB = list[random.randint(0, len(list) - 1)]      #生成B选项
            textC = list[random.randint(0, len(list) - 1)]
            while textC == textA or textC==textB:
                textC = list[random.randint(0, len(list) - 1)]      #生成C选项
            textD = list[random.randint(0, len(list) - 1)]
            while textD == textA or textD == textB or textD==textC:
                textD = list[random.randint(0, len(list) - 1)]      #生成D选项
            self.button_A.setText(textA)
            self.button_A.setStyleSheet("background: rgb(255,255,255)")
            self.button_A.setEnabled(True)                          #A按钮设置
            self.button_B.setText(textB)
            self.button_B.setStyleSheet("background: rgb(255,255,255)")
            self.button_B.setEnabled(True)                          #B按钮设置
            self.button_C.setText(textC)
            self.button_C.setStyleSheet("background: rgb(255,255,255)")
            self.button_C.setEnabled(True)                          #C按钮设置
            self.button_D.setText(textD)
            self.button_D.setStyleSheet("background: rgb(255,255,255)")
            self.button_D.setEnabled(True)                          #D按钮设置
            if text2!=textA and text2!=textB and text2!=textC and text2!=textD:     #如果发现生成的四个选项中没有正确答案，则需要替换掉一个按钮的内容
                rannum_choose=random.randint(1,4)           #依靠随机数来选择替换哪个按钮
                if rannum_choose==1:
                    self.button_A.setText(text2)            #替换A按钮
                elif rannum_choose==2:
                    self.button_B.setText(text2)            #替换B按钮
                elif rannum_choose==3:
                    self.button_C.setText(text2)            #替换C按钮
                else:
                    self.button_D.setText(text2)            #替换D按钮
        list=numsolve()     #执行函数numsolve()
        producechoose(list)     #执行函数producechoose()
        self.label_tip.setText(" ")     #设置，使出题时tip为空
    def checkans(self):
        global rightnum,wrongnum        #初始化
        def rightans(rightnum):         #定义选择正确如何处理
            self.sender().setStyleSheet("background: rgb(0,255,0)")
            rightnum = rightnum + 1
            return rightnum
        def wrongans(wrongnum):         #定义处理错误如何处理
            self.sender().setStyleSheet("background: rgb(255,0,0)")
            wrongnum = wrongnum + 1
            if self.button_A.text() == text2:
                self.button_A.setStyleSheet("background: rgb(0,255,0)")
            elif self.button_B.text() == text2:
                self.button_B.setStyleSheet("background: rgb(0,255,0)")
            elif self.button_C.text() == text2:
                self.button_C.setStyleSheet("background: rgb(0,255,0)")
            else:
                self.button_D.setStyleSheet("background: rgb(0,255,0)")
            return wrongnum
        sender = self.sender().text()       #接受发来的信号并读取文本
        self.label_tip.setText("备注："+text3)     #设置tip的内容
        self.button_A.setEnabled(False)     #让ABCD四个按钮无法选择
        self.button_B.setEnabled(False)
        self.button_C.setEnabled(False)
        self.button_D.setEnabled(False)
        if sender==text2:       #对发来的信号进行处理
            rightnum=rightans(rightnum)
        else:
            wrongnum=wrongans(wrongnum)
        size = int(self.combox_size.currentText().strip("px"))
        self.label_tip.setFont(QFont("", size))
        self.label_right.setText("你答对了{0}道题，".format(rightnum)+"答错了{0}道题，".format(wrongnum)+
                                 "正确率{:.2%}".format(rightnum/(rightnum+wrongnum)))     #显示正确or错误并且展示正确率
    def exittomain(self):       #关闭当前窗口，打开主窗口
        self.win_xuanze.close()
        self.slide_ui=main.parent_page()
        self.slide_ui.win_start.show()
    def layout_init(self):      #定义样式
        self.win_xuanze.setFixedSize(960, 540)
        self.win_xuanze.move(300, 300)
        icon_path=os.getcwd()
        self.win_xuanze.setWindowIcon(QIcon(icon_path+"\\icon\\"+"singlechoose.ico"))
        self.win_xuanze.setWindowTitle("Slide_main")  # 设置界面

        self.button_slide.setText("下一个")
        self.button_slide.clicked.connect(self.randomword)  # 跳转到执行函数randomword
        self.button_slide.move(70, 450)  #设置开始button

        self.button_exittomain.setText("退出")
        self.button_exittomain.clicked.connect(self.exittomain)
        self.button_exittomain.move(790, 450)  # 此三行设置确认button

        self.button_A.setText("请选择其中一项")
        self.button_A.clicked.connect(self.checkans)  # 跳转到执行函数see
        self.button_A.resize(400,50)
        self.button_A.move(40, 225)  # 设置清除button

        self.button_B.setText("请选择其中一项")
        self.button_B.clicked.connect(self.checkans)  # 跳转到执行函数clear
        self.button_B.resize(400, 50)
        self.button_B.move(480, 225)  # 此三行设置清除button

        self.button_C.setText("请选择其中一项")
        self.button_C.clicked.connect(self.checkans)  # 跳转到执行函数confirm
        self.button_C.resize(400, 50)
        self.button_C.move(40,300)  # 设置确认button

        self.button_D.setText("请选择其中一项")
        self.button_D.clicked.connect(self.checkans)
        self.button_D.resize(400, 50)
        self.button_D.move(480, 300)  # 此三行设置确认button

        self.label_explain.move(10, 10)
        self.label_explain.resize(940, 80)
        self.label_explain.setWordWrap(True)
        self.label_explain.setAlignment(Qt.AlignCenter)
        self.label_explain.setText("选择题")
        self.label_explain.setStyleSheet("QLabel{font-size:20px;}")  # 设置label样式
        '''if self.label_explain.text()=="选择题":
            self.excelsolve()'''

        self.label_word.setGeometry(20, 100, 920, 80)
        self.label_word.setWordWrap(True)
        self.label_word.setAlignment(Qt.AlignCenter)
        self.label_word.setStyleSheet("QLabel{background-color: #ffffff;font-size:20px;font-weight:normal;}")  # 设置label样式

        self.label_right.move(0, 0)
        self.label_right.resize(960,30)
        self.label_right.setWordWrap(True)
        self.label_right.setContentsMargins(15, 5, 15, 5)
        self.label_right.setText("你答对了{0}道题，答错了{0}道题".format(rightnum,wrongnum))

        self.label_tip.setGeometry(20,370,920,60)
        self.label_tip.setContentsMargins(15,5,5,5)
        self.label_tip.setWordWrap(True)
        #self.label_tip.setAlignment(Qt.AlignCenter)

        self.combox.setGeometry(10,500,200,30)
        list_mode = ["不重复出题","重复出题",]
        self.combox.addItems(list_mode)

        self.label_tip_size.setGeometry(540, 500, 200, 30)
        self.label_tip_size.setAlignment(Qt.AlignCenter)
        self.label_tip_size.setText("更改备注字号（默认12px）：")

        self.combox_size.setGeometry(750, 500, 200, 30)
        list_size = ["12px", "14px", "15px", "16px", "17px", "18px", "20px", "24px", "28px", "30px", "32px"]
        self.combox_size.addItems(list_size)



def index():
    page = QApplication(sys.argv)
    win = child_page_two()
    win.win_xuanze.show()
    sys.exit(page.exec())

if __name__ == '__main__':
    index()