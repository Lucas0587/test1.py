from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys,json,os,time
class tablelist():
    def __init__(self):
        self.win=QMainWindow()
        self.table_long=QTableWidget(self.win)
        self.button_long_add=QPushButton(self.win)
        self.button_long_fix = QPushButton(self.win)
        self.button_long_del = QPushButton(self.win)
        self.button_long_sav = QPushButton(self.win)
        self.button_long_ope = QPushButton(self.win)
        self.comobox=QComboBox(self.win)
        self.label_note=QLabel(self.win)
        self.layout_init_0()
        self.check_json()
        self.color_set()
        self.win.show()

    def create_json(self):
        with open(file="LongJs.json", mode="w+", encoding="utf-8") as file:
            file.write(json.dumps({"class": [[]]}))
            return 1

    def check_json(self):
        count=0
        if not os.path.exists("LongJs.json"):
            count=self.create_json()
            self.label_note.setText("创建了一个文件哦 ψ(｀∇´)ψ")
            self.explain_label()
        else:
            with open(file="LongJs.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)['class']
            if data == [[]] or data==[] or data==[0]:
                os.remove("LongJs.json")
                count=self.create_json()
                self.explain_label()
                self.label_note.setText("人家还是空空的，快来填满我 q(≧▽≦q)")
        if count!=1:
            with open(file="LongJs.json",mode="r",encoding="utf-8") as file:
                data=json.load(file)['class']
                self.FreshTable(data)

    def FreshTable(self,items):
        for i in range(len(items)):
            item = items[i]
            row = self.table_long.rowCount()
            self.table_long.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.table_long.setItem(row, j, item)
        self.color_set()
        self.label_note.setText("不想干活 ＞﹏＜，如果您不知道如何填写，请填入-，请勿直接点击保存")

    def del_long(self):
        self.table_long.removeRow(self.table_long.currentRow())
        self.label_note.setText("烦人的任务走开了 (*￣3￣)╭")

    def add_list_long(self):
        row = self.table_long.rowCount()
        self.table_long.insertRow(row)
        '''newItem = QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M', time.localtime()))
        self.table_long.setItem(row, 0, newItem)'''
        Itemnew = QTableWidgetItem("-")
        self.table_long.setItem(row, 0, Itemnew)
        Itemnew = QTableWidgetItem("-")
        self.table_long.setItem(row, 1, Itemnew)
        Itemnew=QTableWidgetItem("未完成")
        self.table_long.setItem(row,2,Itemnew)
        Itemnew = QTableWidgetItem("-")
        self.table_long.setItem(row, 3, Itemnew)
        Itemnew = QTableWidgetItem("-")
        self.table_long.setItem(row, 4, Itemnew)
        self.label_note.setText("又要有新任务了 ＞︿＜")

    def save_list_long(self):
        def set_list():
            List = []
            for j in range(self.table_long.columnCount()):
                try:
                    List.append(self.table_long.item(i, j).text())
                except:
                    QMessageBox.warning(self.win, '标题', '保存文件出错')
                    return 0
            return List
        Item_Long=[]
        Item_Finish=[]
        Item_Normal=[]
        Item_Delay=[]
        for i in range(self.table_long.rowCount()):
            if self.table_long.item(i,1).text()=='-':
                Item_Long.append(set_list())
            elif self.table_long.item(i,2).text()=="已完成":
                Item_Finish.append(set_list())
            elif self.table_long.item(i,2).text()=="已过期":
                Item_Delay.append(set_list())
            else:
                Item_Normal.append(set_list())
        Item_Finish.sort(key=lambda Item_Finish: (Item_Finish[1]))
        Item_Normal.sort(key=lambda Item_Normal: (Item_Normal[1]))
        Item_Delay.sort(key=lambda Item_Delay: (Item_Delay[1]))
        Item=Item_Delay+Item_Normal+Item_Long+Item_Finish
        print(Item)
        with open(file='LongJs.json', mode='w', encoding='utf8') as file:
            file.write(json.dumps({"class": Item}))
        self.table_long.setRowCount(0)
        self.table_long.clearContents()
        with open(file="LongJs.json", mode="r", encoding="utf-8") as file:
            data = json.load(file)['class']
            self.FreshTable(data)
        self.color_set()
        QMessageBox.information(self.win, '提示', '保存成功 (∪.∪ )...zzz')

    def time_set(self):
        roww=self.table_long.currentIndex().row()
        col=self.table_long.currentIndex().column()
        def time_con(time):
            try:
                newItem = QTableWidgetItem(time.toString('yyyy-MM-dd hh:mm'))
                self.table_long.setItem(roww, col, newItem)
            except:
                QMessageBox.information(self.win, '提示', 'Something Wrong with time')
        self.timewin=QMainWindow()
        self.TimeEd=QDateTimeEdit(self.timewin)
        self.TimeEd.resize(200,40)
        now_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        self.TimeEd.setDateTime(QDateTime.fromString(now_time, 'yyyy-MM-dd hh:mm'))
        self.TimeEd.dateTimeChanged.connect(time_con)
        self.timewin.show()

    def path_set(self):
        path=QFileDialog.getOpenFileName()
        roww = self.table_long.currentIndex().row()
        col = self.table_long.currentIndex().column()
        newItem = QTableWidgetItem(str(path[0]))
        self.table_long.setItem(roww, col, newItem)

    def path_open(self):
        try:
            path=self.table_long.currentItem().text()
            if os.path.exists(path):
                os.startfile(path)
            else:
                self.label_note.setText("没有这个路径")
        except:
            self.label_note.setText("打开路径出错")

    def color_set(self):
        now_time = time.time()
        for i in range(1,self.table_long.rowCount()+1):
            if self.table_long.item(i-1,1).text()!="-" and self.table_long.item(i-1,2).text()=="未完成" or self.table_long.item(i-1,2).text()=="已过期":
                time_f = time.mktime(time.strptime(str(self.table_long.item(i-1, 1).text()), "%Y-%m-%d %H:%M"))
                difftime=time_f-now_time
                if difftime < 0:
                    self.table_long.setItem(i - 1, 2, QTableWidgetItem("已过期"))
                    for j in range(self.table_long.columnCount()):
                        self.table_long.item(i-1,j).setBackground(QColor('#24fe41'))
                elif difftime < 86400:
                    for j in range(self.table_long.columnCount()):
                        self.table_long.item(i-1,j).setBackground(QColor('#e53935'))
                elif difftime < 172800:
                    for j in range(self.table_long.columnCount()):
                        self.table_long.item(i-1,j).setBackground(QColor('#fdfc47'))
                elif difftime < 259200:
                    for j in range(self.table_long.columnCount()):
                        self.table_long.item(i-1,j).setBackground(QColor('#64b3f4'))

    def explain_label(self):
        self.explain = QMainWindow()
        self.explain.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.explain.setWindowTitle("说明")
        self.explain.setFixedSize(720, 480)
        self.explain_label = QLabel(self.explain)
        self.explain_label.resize(720, 460)
        str = "  1、本程序名为提醒器，旨在通过对用户添加的事项进行整理，以列表的形式呈现。\n" \
              "  2、初次进入程序会自动生成配置文件，点击添加按钮即可添加新的行，在其中输入提醒信息。\n" \
              "  3、输入信息时请务必保证每个单元格都规范填写，截止时间和文件路径若无法确定可填入-，后续进行修改。\n" \
              "  4、输入完成后点击保存按钮即可保存，并根据用户填写的截止时间自动识别：截止时间三天内蓝色、两天内黄色、一天内红色。\n" \
              "  5、设置时间按钮点击即可选择时间，若用户自行填写时间，请按照按钮给定的格式填写，否则无法准确识别时间。\n" \
              "  6、文件地址输入框可双击填入文件或者文件夹地址，但用户需要确保地址正确，否则会无法打开该地址。\n" \
              "  7、下拉菜单栏内点击打开路径之前，请用户确保选中的是地址单元格，否则会无法打开该地址。\n" \
              "  8、用户选中某一单元格，点击删除，即可删除该行内容。需要注意的是，若用户删除之后没有点击保存不等于真正的删除。\n" \
              "  9、请用户修改完操作之后记得及时保存，否则之前的操作无效。保存功能为不可逆操作，请谨慎。\n" \
              "  10、更多疑问，请发送邮件至1648633668@qq.com，感谢您的意见和建议。"
        self.explain_label.setText(str)
        self.explain_label.setWordWrap(True)
        self.explain_label.setContentsMargins(10, 10, 10, 10)
        self.explain_label.setFont(QFont("宋体", 12))
        self.explain.show()

    def fun(self):
        if self.comobox.currentText()=="打开路径":
            self.path_open()
        elif self.comobox.currentText()=="用法说明":
            try:
                self.explain_label()
            except:
                self.label_note.setText("无法调出用法说明，你可以关闭后重新进入（虽然我也不知道为什么）"
                                        "或者查看文件夹中的tip.txt")
        elif self.comobox.currentText()=="更多功能":
            self.label_note.setText("不想干活 ＞﹏＜")

    def layout_init_0(self):      #定义样式
        def Table_style():
            self.table_long.setColumnCount(5)  ##设置表格一共有五列
            self.table_long.setHorizontalHeaderLabels([ '事项','截至日期', '未完成/已完成','文件位置','备注'  ])  # 设置表头文字
            self.table_long.move(10,10)
            self.table_long.resize(940,440)
            self.table_long.setColumnWidth(0, 160)
            self.table_long.setColumnWidth(1, 160)
            self.table_long.setColumnWidth(2, 160)
            self.table_long.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕

        def buttonset_style():
            self.button_long_add.move(20,460)
            self.button_long_add.resize(120,30)
            self.button_long_add.setText("添加")
            self.button_long_add.clicked.connect(self.add_list_long)

            self.button_long_fix.move(200, 460)
            self.button_long_fix.resize(120, 30)
            self.button_long_fix.setText("设置时间")
            self.button_long_fix.clicked.connect(self.time_set)

            self.button_long_ope.move(400, 460)
            self.button_long_ope.resize(120, 30)
            self.button_long_ope.setText("设置路径")
            self.button_long_ope.clicked.connect(self.path_set)

            self.button_long_del.move(600, 460)
            self.button_long_del.resize(120, 30)
            self.button_long_del.setText("删除该项")
            self.button_long_del.clicked.connect(self.del_long)

            self.button_long_sav.move(800, 460)
            self.button_long_sav.resize(120, 30)
            self.button_long_sav.setText("保存")
            self.button_long_sav.clicked.connect(self.save_list_long)

        def buttonfuc():
            self.comobox.move(20,500)
            self.comobox.resize(150,30)
            List=['更多功能','打开路径','用法说明']
            self.comobox.addItems(List)
            self.comobox.activated[str].connect(self.fun)

            self.label_note.move(190,500)
            self.label_note.resize(750,30)
            self.label_note.setText("开始操作吧（￣︶￣）↗　")

        self.win.setWindowTitle('DDL提醒器')
        icon_path=os.getcwd()
        self.win.setWindowIcon(QIcon(icon_path+"\\"+"slide.ico"))
        self.win.setFixedSize(960, 540)
        Table_style()
        buttonset_style()
        buttonfuc()
        '''outerLayout = QVBoxLayout()
        outerLayout.addWidget(self.table_long)
        button_cre_style = QHBoxLayout()
        button_cre_style.stretch(10)
        button_cre_style.addWidget(self.button_long_add)
        button_cre_style.addWidget(self.button_long_fix)
        button_cre_style.addWidget(self.button_long_del)
        button_cre_style.addWidget(self.button_long_sav)
        button_cre_style.addWidget(self.button_long_ope)
        button_fuc_style = QHBoxLayout()
        button_fuc_style.addWidget(self.button_time)
        button_fuc_style.addWidget(self.button_path)
        outerLayout.addLayout(button_cre_style)
        outerLayout.addLayout(button_fuc_style)
        self.win.setLayout(outerLayout)'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = tablelist()
    sys.exit(app.exec_())