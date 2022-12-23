# -*-  codeing = utf-8-*-
# @ Time:12/06/2021 00:58
# @ Author: 四水合铜离子
# @  File: file-0612.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random


'''tup1=()
print(type(tup1))
tup2=(50,)
print(type(tup2))
#元组tup=（对象，），一定要有这个逗号
tup3=(50,60,70)
print(type(tup3))
#多个对象就可以不用关注这个逗号
'''
'''tup4=("abc","dfe",222,333,444,555,666,777)
print(tup4[-1])
print(tup4[1:5])
'''
#增加
'''tup01=(12,34,56)
#tup01[0]=100 'tuple' object does not support item assignment
tup02=("abc","def")
tup=tup01+tup02
print(tup)'''
#删除
'''tup01=(12,34,56)
print(tup01)
del tup01 #直接删除对象
print("shanchuhou:")
print(tup01)'''

info={"name":"fld","age":"18","beauty":"handsome"}
'''print(info["beauty"])
#print(info["gender"]) #直接访问字典里面没有的，会报错
#print(info.get("gender")) #没有的默认返回None
print(info.get("gender"),"m")'''

#增
'''newID=input("请输入：")
info["id"]=newID
print(info["id"])'''
#删
'''print("删除前：%s"%info)
#info.clear()
#del info["name"] #删除的是指定值对
print("删除后：%s"%info)'''
#改
'''info["age"]=20
print(info)'''
#查
#print(info.keys())
#print(info.values())
#print(info.items())
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))

