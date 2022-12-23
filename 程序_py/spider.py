# -*-  codeing = utf-8-*-
# @ Time:18/06/2021 01:38
# @ Author: 四水合铜离子
# @  File: spider.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3
'''alphabe=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
             "r","s","t","u","v","w","x","y","z"]'''
def main():
    #baseurl="http://zhongguose.com/"
    #baseurl="http://movie.douban.com"
    baseurl="https://movie.douban.com/coming"
    #1. 获取数据
    datalist=getData(baseurl)

    #2. 爬取网页
def getData(baseurl):
    dataList=[]
    #若页数很多，在这里有一个for循环，下面解析的过程应该是在for循环里面进行
    url=baseurl
    html = askURL(url)  #保存获取到的网页源码







    savePath=".\\豆瓣最新电影"
    saveData(savePath)

    askURL(baseurl)
    #3. 解析数据
    return dataList

def saveData(savepath):
        print("存储完成")

#得到指定一个url的函数

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"
    }   ##用户代理·表示告诉豆瓣服务器·我们是什么类型的机器·浏览器(本质上是告诉浏览器:我们可T以接收什么水平的文件内容)
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)    #表示能接收回来的响应
        html=response.read().decode("utf-8")    #读取响应信息
        print(html)
    except urllib.error.URLError as e:
        print("访问出错")
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)     #检查报错类型
    return html



if __name__ == "__main__":      #当程序执行时
    main()  #调用主函数