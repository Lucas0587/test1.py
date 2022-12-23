import os,shutil
from PySide2.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QLabel,QMessageBox
from PySide2.QtCore import Qt

Dirs=['File','Image','Thumb','Video']

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.setFixedSize(960, 540)
        self.window.move(300, 300)
        self.window.setWindowTitle('移动微信文件')

        self.label=QLabel(self.window)
        self.label.setText('在下面框内输入微信随意一个文件的路径，\n'
                           '文件路径可在微信随便找到一个文件，右击在文件夹中打开即可找到路径')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(20,30)
        self.label.resize(700,50)
        self.label.setStyleSheet('''font-family:songti;font-size:12pt''')
        self.text = QLineEdit(self.window)
        self.text.move(60, 100)
        self.text.resize(600, 35)
        self.button=QPushButton('确认',self.window)
        self.button.move(700,100)
        self.button.resize(80,35)
        self.button.clicked.connect(self.solve)


    def solve(self):
        fpath = self.text.text()
        fpath_1=os.path.abspath(os.path.join(fpath,"../../../"))
        drawfile(self.window,fpath_1)

def FileMove(file,fpath_new):
    shutil.move(file, fpath_new)
    '''try:
        shutil.move(file,fpath_new)
    except:
        print("有重复文件，或者有其他意外情况")'''

def drawfile(window,fpath_1):
    Message = QMessageBox()
    for i in range(len(Dirs)):
        fpath_Q=fpath_1+"\\"+Dirs[i]
        if not os.path.exists(fpath_Q):
            os.mkdir(fpath_Q)
    try:
        size=os.path.getsize(fpath_1)
        if size==0:
            Message.warning(window, "注意", "该路径下没有文件")
        for i in os.listdir(fpath_1):
            for j in os.listdir(fpath_1 + '\\' + i):
                fpath_new=fpath_1+'\\'+j
                print(fpath_new)
                for k in os.listdir(fpath_1+'\\'+i+'\\'+j):
                    fpath_2=fpath_1+'\\'+i+'\\'+j+'\\'+k
                    for file in os.listdir(fpath_2):
                        print(file)
                        FileMove(file,fpath_new)
    except:
        Message.warning(window,"注意","路径错误")

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()