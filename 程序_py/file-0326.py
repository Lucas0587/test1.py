# -*-  codeing = utf-8-*-
# @ Time:26/03/2021 14:59
# @ Author: 四水合铜离子
# @  File: file-0326.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

'''
#1-n求积
n=input("请输入数据:")
n=int(n)
sum=1
i=1
while i<=n:
    sum=sum*i
    i+=1
print("1-%d的积为：%d"%(n,sum))
count=1
while count<5:
    print(count,"小于等于5")
    count+=1
else:
    print(count,"大于或等于5")
'''
'''
i=0
while i<10:
    i+=1
    print("-"*30)   #"-"*30表示将其循环30次
    if i==5:
        break
        #pass
        #continue
    print(i)
'''

'''
for i in range(1,10,1):
    for j in range(1,i+1,1):
        print("%d*%d=%d"%(j,i,i*j),end="\t")
        j+=1
    print("",end="\n")
    i+=1
para="""
    碱金属与碱土金属化学性质活泼，在自然界中均以化合态形式存在。其中钠、钾丰度在地壳中分布广泛，丰度均为2.5%。
    碱金属与碱土金属主要矿物有：钠长石Na[AlSi3O8]、
    光卤石KCl·MgCl2·6H2O、锂辉石Li2O·Al2O3·4SiO2、绿柱石3BeO·Al2O3·6SiO2、
    白云石CaCO3·MgCO3、菱镁矿MgCO3、方解石CaCO3、
    石膏CaSO4·2H2O、天青石SrSO4和重晶石BaSO4。
"""
print(para)
'''
str="shanghai"
print(str[3]*3)
print(str[0:8:1]) #[初始位置：结束位置：步进值]
print(r"hello\nChina")  #r将转义字符转化成文本输出
