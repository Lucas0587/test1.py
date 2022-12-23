# -*-  codeing = utf-8-*-
# @ Time:17/06/2021 14:23
# @ Author: 四水合铜离子
# @  File: file-0617.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

#try，finally嵌套
import time
try:
    f=open("file-0321.py","w")
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常")