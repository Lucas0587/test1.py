from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,\
    QPlainTextEdit,QMessageBox,QFrame,QLineEdit,QFormLayout,QLabel,QComboBox,\
    QDateTimeEdit,QTableWidget,QTableWidgetItem
from PySide2.QtCore import Qt,QDateTime,QCoreApplication
import json

class Stats():      #定义类
    def __init__(self):
        self.window = QMainWindow()
        self.window.setFixedSize(960, 540)
        self.window.move(300, 300)
        self.window.setWindowTitle('DDL显示器')

        self.frame1=QFrame(self.window)
        self.frame1.resize(620,120)
        self.frame1.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.frame1.setStyleSheet("background-color:#F4DAF0")
        self.frame1.Label1=QLabel(self.window)
        self.frame1.Label1.setText('事项')
        self.frame1.Label1.setAlignment(Qt.AlignCenter)
        self.frame1.Label1.move(20,20)
        self.frame1.Label2 = QLabel(self.window)
        self.frame1.Label2.setText('截止时间')
        self.frame1.Label2.setAlignment(Qt.AlignCenter)
        self.frame1.Label2.move(220, 20)
        self.frame1.Label3 = QLabel(self.window)
        self.frame1.Label3.setText('紧急度')
        self.frame1.Label3.setAlignment(Qt.AlignCenter)
        self.frame1.Label3.move(420, 20)
        self.frame1.text=QLineEdit(self.window)
        self.frame1.text.move(20,60)
        self.frame1.text.resize(140, 30)
        self.frame1.time=QDateTimeEdit(QDateTime.currentDateTime(), self.window)
        self.frame1.time.setDisplayFormat("MM/dd HH:mm")
        self.frame1.time.setCalendarPopup(True)
        self.frame1.time.move(220,60)
        self.frame1.time.resize(140, 30)
        self.frame1.box=QComboBox(self.window)
        self.frame1.box.move(420,60)
        self.frame1.box.resize(140,30)
        self.frame1.box.addItems(['!!! 非常重要','!! 重要','!一般'])

        self.frame2=QFrame(self.window)
        self.frame2.setGeometry(620,0,340,120)
        self.frame2.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.frame2.setStyleSheet("background-color:#FFC6C9")
        self.frame2.button1=QPushButton('添加', self.window)
        self.frame2.button1.move(630, 20)
        self.frame2.button1.clicked.connect(self.solve)
        self.frame2.button2 = QPushButton('保存', self.window)
        self.frame2.button2.move(740, 20)
        self.frame2.button2.clicked.connect(self.saveData)
        self.frame2.button3 = QPushButton('查询', self.window)
        self.frame2.button3.move(630, 60)
        self.frame2.button3.clicked.connect(self.solve)
        self.frame2.button4 = QPushButton('修改', self.window)
        self.frame2.button4.move(740, 60)
        self.frame2.button4.clicked.connect(self.solve)
        self.frame2.button5 = QPushButton('导入导出', self.window)
        self.frame2.button5.move(850, 60)
        self.frame2.button5.clicked.connect(self.saveData)

        self.frame3=QFrame(self.window)
        self.frame3.setGeometry(0, 120, 960, 420)
        self.frame3.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.frame3.setStyleSheet("background-color:#C1F5FC")
        self.frame3.table=QTableWidget(self.window)
        self.frame3.table.setGeometry(0, 120, 960, 420)

        self.frame3.table.setColumnCount(5)
        item = QTableWidgetItem()
        self.frame3.table.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.frame3.table.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.frame3.table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.frame3.table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.frame3.table.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.frame3.table.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.frame3.table.setHorizontalHeaderItem(4, item)
        _translate = QCoreApplication.translate
        item = self.frame3.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.frame3.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "相关事项"))
        item = self.frame3.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "截止时间"))
        item = self.frame3.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "重要程度"))
        item = self.frame3.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "备注"))
        #self.verticalLayout.addWidget(self.frame3.table)

        try:
            self.openDefaultData()
        except:
            pass

    def openDefaultData(self):
        '''打开默认文件信息'''
        with open(file='stuMsg.json', mode='r', encoding='utf8') as file:
            items = json.load(file)['class']
            self.frame3.table.setRowCount(0)
            self.frame3.table.clearContents()
            self.freshTable(items)

    def solve(self):
        text = self.frame1.text.text()
        time=self.frame1.time.dateTime()
        box=self.frame1.box.currentText()
        if '!!!' in box:
            box_level=3
        elif '!!' in box:
            box_level=2
        else:
            box_level=1
        items=[[text],[time.toString(Qt.ISODate).replace('T',' ')],[box],[box_level]]
        for i in range(self.frame3.table.rowCount()):
            lis = []
            for g in range(self.frame3.table.columnCount()):  # 此处是7行
                if self.frame3.table.item(i, g):
                    lis.append(self.frame3.table.item(i, g).text())
            items.append(lis)
        print(items)
        QMessageBox.about(self.window,'///','已储存')

    def saveData(self):
        '''保存默认文件信息'''
        items = []
        for i in range(self.frame3.table.rowCount()):
            lis = []
            for g in range(self.frame3.table.columnCount()):  # 此处是7行
                if self.frame3.table.item(i, g):
                    lis.append(self.frame3.table.item(i, g).text())
            items.append(lis)
        with open(file='stuMsg.json', mode='w+', encoding='utf8') as file:
            file.write(json.dumps({"class": items}))
            QMessageBox.information(self.window, '通知', '数据保存成功')
        print(items)

    def freshTable(self, items):
        '''主界面table刷新模块'''
        print(items)
        for i in range(len(items)):
            item = items[i]
            row = self.frame3.table.rowCount()
            self.frame3.table.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.frame3.table.setItem(row, j, item)

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()