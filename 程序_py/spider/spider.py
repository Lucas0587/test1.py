import requests
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
}
def get_info(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    content=soup.select('#app > div.article-container > div.article-wrapper > div.article.article-detail > p:nth-child(6) > span > img')
    print(type(content))

if __name__=='__main__':
    url='https://wap.peopleapp.com/article/6829071/6696766'
    get_info(url)
    time.sleep(1)
