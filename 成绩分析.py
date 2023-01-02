import xlrd,os
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
import numpy as np
fig,ax=plt.subplots(figsize=(9.6,5.4))

def ReadData():
    ListData=[]
    FilePath=os.getcwd()+"\\"+"成绩分析.xlsx"
    SheetBook = xlrd.open_workbook(FilePath)  # 打开表格
    SheetName = SheetBook.sheet_names()  # 获取名称
    SheetData = SheetBook.sheet_by_name(SheetName[0])  # 获取表格内容
    NumRows = SheetData.nrows  # 获取表格列数，由于第一行非内容行，因此实际items会比num_rows少1
    for i in range(0,NumRows):
        ListData.append([SheetData.cell_value(i,1),SheetData.cell_value(i,2),SheetData.cell_value(i,4),
                         SheetData.cell_value(i,5),SheetData.cell_value(i,6)])
    return ListData

def PreAnalysisData(ListData):
    Term=[]
    Term.append(ListData[1][3])
    for i in range(1,len(ListData)):
        TermTemp=ListData[i][3]
        if TermTemp not in Term:
            Term.append(TermTemp)
    return Term

def AnalysisData(ListData):

    def GPAAnalysis(TermAquire):
        point, sumproduct = 0, 0
        for i in range(1, len(ListData)):
            if ListData[i][3] == TermAquire:
                point += ListData[i][1]
                sumproduct += ListData[i][1] * ListData[i][2]
        GPA=round(sumproduct/point,2)
        return GPA

    def BarPlot(xlabel,GPAList,Term):
        p1 = ax.bar(xlabel, GPAList, width=0.35, color="#a4cab6", linewidth=0.35)
        ax.set_xticks(xlabel, labels=Term)
        ax.bar_label(p1, label_type='edge', padding=5, fontsize=12)
        plt.ylim((3.2, 4.0))
        plt.yticks(np.arange(3.2, 4.0, 0.1))
        plt.show()

    def LinePlot(Term, GPAList):
        plt.subplots(figsize=(9.6, 5.4))
        p2 = plt.plot(Term, GPAList, marker='.', markersize=8)
        plt.ylim((3.2, 4.0))
        plt.yticks(np.arange(3.2, 4.0, 0.1))
        plt.xticks(rotation=30)
        plt.grid()
        # plt.margins(0.2)
        plt.show()

    def PiePlot(ListData):
        Course = []
        for i in range(0, len(ListData)):
            if ListData[i][4] == "专业课":
                Course.append([ListData[i][0], ListData[i][1], ListData[i][2]])
        CourseTemp = {}
        for i in range(len(Course)):
            if CourseTemp.__contains__(Course[i][2]) == False:
                CourseTemp[Course[i][2]] = 1
            else:
                CourseTemp[Course[i][2]] += 1
        CourseTemp = dict(sorted(CourseTemp.items(), key=lambda CourseTemp: CourseTemp[0], reverse=True))
        fig1, ax1 = plt.subplots(figsize=(9.6, 5.4))
        explode, temp = (0.05,), (0,)
        for i in range(len(CourseTemp) - 1):
            explode += temp
        labels = list(CourseTemp.keys())
        sizes = list(CourseTemp.values())
        ax1.pie(sizes, labels=labels, autopct='%0.1f%%', textprops={'fontsize': 12, 'fontfamily': 'Arial'},
                startangle=90, colors=["#12c2e9", "#c471ed", "#F27121", "#54B1F7", "#3EF0D0", "#ff11ff"],
                explode=explode)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def LinePlotTwo(ListData):
        Course , data = {},[]
        for i in range(0, len(ListData)):
            if ListData[i][4] == "通识课":
                Course[ListData[i][0]]=round(ListData[i][2],1)
        xlabel=np.arange(len(Course))
        fig2, ax2 = plt.subplots(figsize=(9.6, 5.4))
        p1 = ax2.bar(xlabel, list(Course.values()), width=0.35, color="#a4cab6", linewidth=0.35)
        ax2.set_xticks(xlabel, labels=list(Course.keys()))
        ax2.bar_label(p1, label_type='edge', padding=5, fontsize=12,labels=list(Course.values()))
        plt.ylim((0, 4.3))
        plt.yticks(np.arange(0, 4.3, 0.5))
        plt.xticks(rotation=14)
        plt.show()

    Term=PreAnalysisData(ListData)
    TermNumber = len(Term)
    xlabel=np.arange(TermNumber)
    GPAList=[]
    for i in range(len(Term)):
        GPA=GPAAnalysis(Term[i])
        GPAList.append(GPA)
    BarPlot(xlabel, GPAList, Term)
    LinePlot(Term, GPAList)
    PiePlot(ListData)
    LinePlotTwo(ListData)

def main():
    ListData=ReadData()
    AnalysisData(ListData)

if __name__ == '__main__':
    main()