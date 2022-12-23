#-*-  codeing = utf-8-*-
#@ Time:2022/3/17 18:13
#@ Author: 四水合铜离子
#@  File: file_0317(2022).py
#@Software: PyCharm
#import pandas as pd
import numpy as np
#import random

from bs4 import BeautifulSoup   #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定url，获取数据
import xlwt #进行excel操作
import sqlite3  #进行SQLite数据库操作

subject=[-1,1,2,3,4,5,6,7,8,9,10]
#print(subject[0:-1:2])

score=np.array([[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20]])
print(score[subject=='2',subject=='2'])