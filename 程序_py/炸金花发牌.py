# -*-  codeing = utf-8-*-
# @ Time:18/08/2021 12:04
# @ Author: 四水合铜离子
# @  File: 炸金花发牌.py.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
# import random

'''from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作'''

import random

poker = []
player_list = []
player_dic = {}
suit_list = ["", "", "", ""]
point_list = list(range(2, 11))
for point in point_list:
    point_list[point_list.index(point)] = str(point)
point_list.extend(['J', 'Q', 'K', 'A'])
print(suit_list)
print(point_list)

def set_poker():
    """
    创建扑克牌
    :return:
    """
    for i in suit_list:
        for j in point_list:
            poker.append([i + str(j)])

def set_player():
    """
    设置玩家
    :return:
    """
    player_num = int(input("请输入游戏人数：").strip())
    for i in range(player_num):
        player_list.append(input(f"请输入玩家{i+1}的姓名：").strip())

def get_card():
    """
    发牌程序，每人发三张牌，不重复
    :return:
    """
    for i in player_list:
        player_dic[i] = random.sample(poker, 3)
        for j in player_dic[i]:
            poker.remove(j)

def card_sort():
    for i in player_dic:
        if point_list.index(player_dic[i][0][0][1:]) > point_list.index(player_dic[i][1][0][1:]):
            temp = player_dic[i][0]
            player_dic[i][0] = player_dic[i][1]
            player_dic[i][1] = temp
        if point_list.index(player_dic[i][1][0][1:]) > point_list.index(player_dic[i][2][0][1:]):
            temp = player_dic[i][1]
            player_dic[i][1] = player_dic[i][2]
            player_dic[i][2] = temp
        if point_list.index(player_dic[i][0][0][1:]) > point_list.index(player_dic[i][1][0][1:]):
            temp = player_dic[i][0]
            player_dic[i][0] = player_dic[i][1]
            player_dic[i][1] = temp

# def typ():
#     for i in player_dic:
#         if player_dic[i][0][0][1:] == player_dic[i][0][1][1:] == player_dic[i][0][2][1:]:
#             player_dic[i][0].append("豹子")
#         elif player_dic[i][0][0][0] == player_dic[i][0][1][0] == player_dic[i][0][2][0]:
#             if point_list.index(player_dic[i][0][0][1:]) + 1 == point_list.index(player_dic[i][0][1][1:])\
#                     == point_list.index(player_dic[i][0][2][1:]) - 1 or \
#                     player_dic[i][0][0][1:] == '2' and player_dic[i][0][1][1:] == '3' and player_dic[i][0][2][1:] == '1':
#                 player_dic[i][0].append("同花顺")
#             else:
#                 player_dic[i][0].append("同花")

set_poker()
print(poker)
set_player()
get_card()
card_sort()
print("发牌结果：")
for index in player_dic:
    print(f"{index}:{player_dic[index]}")