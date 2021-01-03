# -*- coding = utf-8 -*-
# @Time : 2020/10/11 14:07
# @Author : TianChi
# @File : 1.py
# @Software : PyCharm



from bs4 import BeautifulSoup   # 网页解析，获取数据
import re   # 正则表达式，进行文字匹配
import urllib.request,urllib.error   # 指定URL，获取网页数据
import xlwt    # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

find_link = re.compile(r'<a href="(.*?)">')

soup = BeautifulSoup(html,"html.parser")
for item in soup.find_all("div",class_="item"):
    data = []
    item = str(item)
    link = re.findall(find_link,item)[0]


find_link = re.compile(r'<a href="(.*?)">')

soup = BeautifulSoup(html,"html.parser")
for item in soup.find_all("div",class_="item"):
    data = []
    item = str(item)
    link = re.findall(find_link,item)[0]



