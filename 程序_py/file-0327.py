# -*-  codeing = utf-8-*-
# @ Time:27/03/2021 16:26
# @ Author: 四水合铜离子
# @  File: file-0327.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random
nameList=['1','2','3']
'''
print(len(nameList))
for name in nameList:
    print(name)'''

#增加 1.append:在末尾追加
#     2.extend:扩充填入
#     3.insert:将元素i插入下标为j位置上
list=['1','2','3','4','5']
'''
print('---增加前---')
for name in list:
    print(name)
nametemp=input("请输入 ：")
list.append(nametemp)
print('---增加后---')
'''
'''
提醒：
a=[1,2]
b=[3,4]
a.append(b)
print(a)
最后输出的是[1, 2, [3, 4]]
'''
'''a=[1,2]
b=[3,4]
a.extend(b)
print(a)
最后输出的是[1, 2, 3, 4]'''

'''
list.insert(1,'3')
for name in list:
    print(name)
    
'''
#删除 1.del:删除指定位置的元素
#     2.pop:删除溢出元素，即最后一个
#     3.remove:删除指定内容的元素
listl=['02','20','40','60','80','20','40']
'''
#del listl[2]
#listl.pop()
listl.remove('20')
for name in listl:
    print(name)
'''
#修改：
'''
nameList[1]='10'
for name in nameList:
    print(name)
'''
#查找:1.直接找
#     2.index():查到下标
'''
findName=input('查找：')
if findName in nameList:    #如果不在，那就是not in
    print("找到")
else:
    print("没有找到")
print(listl.index('20',0,len(listl)+1))
print(listl.count('20'))
'''
#排序：1.reverse()
#     2.sort()
'''
listl.reverse()
print(listl)
listl.sort()
print(listl)
listl.sort(reverse=True)#降序
print(listl)
'''
#二维数组形式
'''
listli=[['1','2','3'],['01','02','03'],['001','002']]
print(listli[1][2])
'''
'''import random
offices=[[],[],[],[]]
names=['A','B','C','D','E','F','G','H','I','J','K']
for name in names:
    index=random.randint(0,3)
    offices[index].append(name)
i=1
for office in offices:
    print('办公室30%d的人数为：%d'%(i,len(office)))
    i+=1
    for name in office:
        print('%s'%name,end='\t')
    print('\n')'''

