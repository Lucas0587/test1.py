import os,shutil,fitz,time,sys,requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class qt():
    def __init__(self):
        self.win=QMainWindow()
        self.label_explain_path=QLabel(self.win)
        self.pathinput=QLineEdit(self.win)
        self.label_setpath = QLabel(self.win)
        self.button_path=QPushButton(self.win)
        self.label_path=QLabel(self.win)
        self.label_explain_name = QLabel(self.win)
        self.nameinput = QLineEdit(self.win)
        self.button_start = QPushButton(self.win)
        self.button_clear=QPushButton(self.win)
        self.label_pro=QLabel(self.win)
        self.label_progre=QLabel(self.win)
        self.layouy_init()
        self.win.show()

    def path_select(self):      #定义设置路径函数
        path=QFileDialog.getExistingDirectory()
        self.label_path.setText(path)

    def download(self,url,file_path,path):      #定义下载图片函数
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44",
        }
        r = requests.get(url, headers=headers)
        with open(file_path, "wb") as f:
            f.write(r.content)
        time.sleep(0.5)
        shutil.move(file_path, path)

    def pdff(self,path,now_page,name):      #定义制作pdf函数
        os.chdir(path)
        doc = fitz.open()
        for i in range(1,now_page):
            img = str(i) + '.png'
            try:
                imgdoc = fitz.open(img)
            except:
                print(1+1+2)
            try:
                pdfbytes = imgdoc.convertToPDF()
                pdf_name = str(i) + '.pdf'
                imgpdf = fitz.open(pdf_name, pdfbytes)
                doc.insertPDF(imgpdf)
            except:
                print(1+2)
        doc.save(name+'.pdf')
        doc.close()

    def clear(self):
        self.label_path.setText("")
        self.pathinput.setText("")
        self.nameinput.setText("")

    def start(self):        #定义初始函数
        if self.pathinput.text()=="":
            QMessageBox.information(self.win, "提示", "您未输入图片地址")
            return 0
        url = ""
        page_now=1
        file_name=self.nameinput.text()
        if file_name=="":
            file_name=time.strftime("%Y-%m-%d %H-%M", time.localtime())
        file_path=self.label_path.text()
        if file_path=="":
            file_path=os.getcwd()
        path = file_path + "\\" + file_name
        if not os.path.exists(path):
            os.mkdir(path)
        prefix_url=self.pathinput.text()
        prefix_url_list = prefix_url.split('/')
        for i in range(len(prefix_url_list) - 1):
            url = url + prefix_url_list[i] + "/"
        if requests.get(url+str(page_now)+'.png').status_code!=200:
            QMessageBox.information(self.win, "提示", "爬虫状态码为{}".format(requests.get(url + str(page_now) + '.png').status_code))
            return 0
        while requests.get(url+str(page_now)+'.png').status_code==200:
            try:
                self.download(url+str(page_now)+'.png',str(page_now)+'.png',path)
                page_now+=1
            except:
                QMessageBox.information(self.win, "提示", "爬虫状态码为{}".format(requests.get(url+str(page_now)+'.png').status_code))
                return 0
        self.pdff(path,page_now,file_name)
        choice=QMessageBox.question(self.win,"Question","是否删除过程中下载的图片", QMessageBox.Yes | QMessageBox.No)
        if choice ==QMessageBox.Yes:
            for i in range(1,page_now):
                try:
                    os.remove(path+"\\"+str(i)+'.png')
                except:
                    print(1+2)

    def layouy_init(self):      #定义界面设置函数
        self.win.setFixedSize(960,540)
        self.win.setWindowTitle("PicDownloader")
        self.win.setStyleSheet("QWidget{background-color: #e7f0fd;}")

        self.label_explain_path.move(20,30)
        self.label_explain_path.resize(920,40)
        self.label_explain_path.setAlignment(Qt.AlignLeft)
        self.label_explain_path.setText("请输入pdf任意一页图片链接，例如：\n    https://s3.ananas.chaoxing.com/sv-w8/doc/10/6a/cb/0bbc7da3c305b47148f3b87872069668/thumb/105.png")

        self.pathinput.move(20, 80)
        self.pathinput.resize(920, 30)
        self.pathinput.setStyleSheet("QLineEdit{background-color: #ffffff;}")

        self.label_setpath.move(20, 140)
        self.label_setpath.resize(300, 30)
        self.label_setpath.setAlignment(Qt.AlignRight)
        self.label_setpath.setText("请选择文件路径，默认为当前文件夹：")
        self.label_setpath.setWordWrap(True)

        self.button_path.move(340,130)
        self.button_path.resize(120,30)
        self.button_path.setText("选择")
        self.button_path.clicked.connect(self.path_select)
        self.button_path.setStyleSheet("QPushButton{background-color:#9face6}")

        self.label_path.move(480, 120)
        self.label_path.resize(460, 40)

        self.label_explain_name.move(20, 200)
        self.label_explain_name.resize(300, 40)
        self.label_explain_name.setAlignment(Qt.AlignRight)
        self.label_explain_name.setText("请输入文件名，默认名为当前时间")
        self.label_explain_name.setWordWrap(True)

        self.nameinput.move(340, 190)
        self.nameinput.resize(600, 30)
        self.nameinput.setStyleSheet("QLineEdit{background-color: #ffffff;}")

        self.button_start.move(20, 260)
        self.button_start.resize(120, 30)
        self.button_start.setText("开始")
        self.button_start.clicked.connect(self.start)
        self.button_start.setStyleSheet("QPushButton{background-color:#9face6}")

        self.button_clear.move(150, 260)
        self.button_clear.resize(120, 30)
        self.button_clear.setText("清空")
        self.button_clear.clicked.connect(self.clear)
        self.button_clear.setStyleSheet("QPushButton{background-color:#9face6}")

        self.label_pro.move(280,260)
        self.label_pro.resize(750,30)
        self.label_pro.setText("- - - - - - - - - - - - - - - - - - 注意事项 - - - - - - - - - - - - - - - - - -")
        #self.label_pro.setAlignment(Qt.AlignCenter)

        self.label_progre.move(20,320)
        self.label_progre.resize(920,200)
        self.label_progre.setStyleSheet("QLabel{background-color: #accbee;}")  # 设置label样式
        str="1、工作原理：利用requests库通过图片链接下载图片,利用fitz库制作pdf\n" \
            "2、由于利用爬虫进行下载图片，因此设置爬虫间隔0.5s，防止被拒绝访问\n" \
            "3、爬虫过程会出现“假死”，即显示未响应，请耐心等待至出现提示窗口"
        self.label_progre.setText(str)
        self.label_progre.setContentsMargins(20, 20, 20, 20)
        self.label_progre.setFont(QFont("宋体", 12))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=qt()
    sys.exit(app.exec_())