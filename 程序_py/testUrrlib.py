# -*-  codeing = utf-8-*-
# @ Time:18/06/2021 12:13
# @ Author: 四水合铜离子
# @  File: testUrrlib.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

#get请求
#response=urllib.request.urlopen("http://baidu.com")
#print(response)
#print(response.read())
#print(response.read().decode("utf-8"))

#post请求
# import urllib.parse     #解析
# data = bytes(urllib.parse.urlencode({"hello":"world","name":"FLD"}),encoding="utf-8")    #data表单封装的信息会在下面返回出来
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response=urllib.request.urlopen("http://baidu.com",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

#响应头
# response=urllib.request.urlopen("http://douban.com")
# print(response.status)
'''response=urllib.request.urlopen("http://www.baidu.com")
print(response.getheader("Server"))
print(response.getheaders())'''

#伪装成浏览器
'''
url="http://httpbin.org/post"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"
}
data=bytes(urllib.parse.urlencode({"name":"FLD"}),encoding="utf-8")
req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")     #构建请求对象
response=urllib.request.urlopen(req)    #构建响应对象
print(response.read().decode("utf-8"))  #打印请求对象
'''
'''url="http://zhongguose.com/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"
}
req=urllib.request.Request(url=url,headers=headers)     #构建请求对象
response=urllib.request.urlopen(req)    #构建响应对象
print(response.read().decode("utf-8"))  #打印请求对象'''