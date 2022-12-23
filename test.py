from collections import OrderedDict
import pandas as pd

def readtxt(filename):
    fp = open(filename, "r")
    sample = fp.readlines()
    result_dict = {}
    key=[]
    value=[]
    for line in sample:
        value_=[]
        line = str(line).replace("\n", "")
        sample_ = line.split(',')#按俩空格进行文件中每一行的切割
        key_ = sample_[0].split(':')
        key.append(key_[0])
        value_.append(float(key_[1]))
        for i in range(1,len(sample_)):
            value_.append(float(sample_[i]))
        value.append(value_)
    result_dict = dict(zip(key,value))
    return result_dict
examDict = readtxt("1.txt")
examOrderDict=OrderedDict(examDict)
examDf=pd.DataFrame(examOrderDict)

print(examDf.head())


#提取特征和标签
#特征features
exam_X=examDf.loc[:,'Study_time']
#标签labes
exam_y=examDf.loc[:,'Score']

#绘制散点图
import matplotlib.pyplot as plt

#散点图
plt.scatter(exam_X, exam_y, color="b", label="exam data")

#添加图标标签
plt.xlabel("Hours")
plt.ylabel("Score")
#显示图像
plt.show()

#相关系数：corr返回结果是一个数据框，存放的是相关系数矩阵
rDf=examDf.corr()
print('相关系数矩阵：')
print(rDf)

'''
train_test_split是交叉验证中常用的函数，功能是从样本中随机的按比例选取训练数据（train）和测试数据（test）
第一个参数：所要划分的样本特征
第2个参数：所要划分的样本标签
train_size：训练数据占比，如果是整数的话就是样本的数量
'''
from sklearn.model_selection import train_test_split

#建立训练数据和测试数据
X_train , X_test , y_train , y_test = train_test_split(exam_X ,
                                                       exam_y ,
                                                       train_size = .8)
#输出数据大小
print('原始数据特征：',exam_X.shape ,
      '，训练数据特征：', X_train.shape , 
      '，测试数据特征：',X_test.shape )

print('原始数据标签：',exam_y.shape ,
      '训练数据标签：', y_train.shape ,
      '测试数据标签：' ,y_test.shape)
#绘制散点图
import matplotlib.pyplot as plt

#散点图
plt.scatter(X_train, y_train, color="blue", label="train data")
plt.scatter(X_test, y_test, color="red", label="test data")

#添加图标标签
plt.legend(loc=2)
plt.xlabel("Hours")
plt.ylabel("Score")
#显示图像
plt.show()

#模型训练
#将训练数据特征转换成二维数组XX行*1列
X_train=X_train.values.reshape(-1,1)
#将测试数据特征转换成二维数组行数*1列
X_test=X_test.values.reshape(-1,1)

#第1步：导入线性回归
from sklearn.linear_model import LinearRegression
# 第2步：创建模型：线性回归
model = LinearRegression()
#第3步：训练模型
model.fit(X_train , y_train)
#截距
a=model.intercept_
#回归系数
b=model.coef_
print('最佳拟合线：截距a=',a,'，回归系数b=',b)

#绘图
#训练数据散点图
plt.scatter(X_train, y_train, color='blue', label="train data")

#训练数据的预测值
y_train_pred = model.predict(X_train)
#绘制最佳拟合线
plt.plot(X_train, y_train_pred, color='black', linewidth=3, label="best line")

#添加图标标签
plt.legend(loc=2)
plt.xlabel("Hours")
plt.ylabel("Score")
#显示图像
plt.show()

#线性回归的scroe方法得到的是决定系数R平方
#评估模型:决定系数R平方
print(model.score(X_test , y_test))
'''
score内部会对第一个参数X_test用拟合曲线自动计算出y预测值，内容是决定系数R平方的计算过程。所以我们只用根据他的要求输入参数即可。
'''
