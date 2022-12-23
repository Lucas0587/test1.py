# -*-  codeing = utf-8-*-
# @ Time:2022/12/23 14:08
# @ Author: 四水合铜离子
# @  File: 带标签的直线图.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
