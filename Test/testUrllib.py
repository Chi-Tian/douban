# -*- coding = utf-8 -*-
# @Time : 2020/10/10 17:34
# @Author : TianChi
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request

# 获取一个get请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行utf-8解码


# 获取一个post请求

# import urllib.parse    # parse是一个解析器，将键值对按照一定的格式（例如utf-8）进行一个解析，然后用bytes()方法转换为二进制，封装到数据包里
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data= data)
# print(response.read().decode('utf-8'))

# 超时处理    在timeout=''指定的时间内如果没有反应，就停止或者不爬取了

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print('time out!')


#
# response = urllib.request.urlopen('http://httpbin.org/get')
# response = urllib.request.urlopen('http://douban.com')   # urllib.error.HTTPError: HTTP Error 418:  报这样的错误说明对方知道你是爬虫了
# response = urllib.request.urlopen('http://baidu.com')
# print(response.status)   # 显示此次访问的状态码
# print(response.getheader('Server'))  # 获取此次访问的标题


# 向httpbin.org网站发送一个post请求，模式为POST
# url = 'https://www.httpbin.org/post'
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge) Chrome/85.0.4183.121 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name" : "eric"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))


# 爬取豆瓣网页源码 模式为get
url = 'https://www.douban.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge) Chrome/85.0.4183.121 Safari/537.36"}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))