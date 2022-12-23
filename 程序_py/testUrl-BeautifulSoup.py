# -*-  codeing = utf-8-*-
# @ Time:21/06/2021 09:04
# @ Author: 四水合铜离子
# @  File: testUrl-BeautifulSoup.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

'''BeautifulSoup4将复杂HTML文档转换成—个复杂的树形结构,每个节点都是Python对象，所有对象可以归纳为4种:
- Tag
- NavigableString
- BeautifulSoup
- Comment'''

file = open("即将上映电影.html","rb")
html = file.read()  #读取
bs = BeautifulSoup(html,"html.parser")  #需要一个指定的解析器：html文件，用html.parser解析器

#Tag
print(type(bs.head))
print(bs.title.string)
#默认直接拿到第一个


#NavigatleString
print(type(bs.title.string))


#键值对    print(bs.a.attrs)

#BeautifulSoup
print(type(bs))
print(bs.name)
print(bs.attrs)

#Comment
print(bs.a.string)