# -*-  codeing = utf-8-*-
# @ Time:2022/4/16 15:32
# @ Author: 四水合铜离子
# @  File: test1.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

'''from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import tkinter
from tkinter import *
top = Tk()
L1 = Label(top, text="网站名")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)
top.mainloop()'''

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
    if counter > 6:
        print('很遗憾你没有get到答案')
        print('正确答案为',answer)
        break
print('你总共猜了%d次' % counter)
