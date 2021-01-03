# -*- coding = utf-8 -*-
# @Time : 2020/10/10 20:50
# @Author : TianChi
# @File : testBs4.py
# @Software : PyCharm

'''
BeautifulSoup4 将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
1.Tag
2.NavigableString
3.BeautifulSoup
4.Comment
'''

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")  # ./ 表示文件在当前目录下
html = file.read().decode('utf-8')   # 将读出来的信息存储到一个html文档
bs = BeautifulSoup(html,"html.parser")   # 解析html文件，用html.parser这个解析器来解析，形成一个文件树

# 按照标签来打印
print(bs.title)
print(bs.a)
print(bs.head)

print('-'*40)

# 1.tag  标签及其内容，但是只能拿到他所找到的第一个内容
print(type(bs.head))   # <class 'bs4.element.Tag'>

print('-'*40)

# 2.NavigableString  指标签里的内容（就是字符串）
print(bs.title.string)
print(type(bs.title.string))   # <class 'bs4.element.NavigableString'>

print(bs.a.attrs)  # 用这个方法快速拿到一个标签里的所有属性，以字典的形式存储

print('-'*40)

# 3.BeautifulSoup  表示整个文档
print(bs)
print(type(bs))
print(bs.name)  # [document]
print(bs.attrs)  # {} 空的

print('-'*40)

# 4.Comment   是一个特殊的NavigableString ，输出的内容不包括注释符号
print(bs.a.string)
print(type(bs.a.string))  # <class 'bs4.element.Comment'>

print('-'*80)

# --------------------------------------------------------------
# 文档的遍历  （更多内容参考 遍历文档树）
print(bs.head.contents)  # contents  获取Tag的所有子节点，返回一个list（将head标签里的内容全部打印出来，并且存储在一个数组中）
print(bs.head.contents[1])  # 拿到head标签里的第2个内容

print('-'*80)

# 文档的搜索（重点）
# (1).find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")
print(t_list)

print('-'*80)

# 正则表达式搜索：使用search()方法来匹配内容
import re
t_list = bs.find_all(re.compile("a"))  # 利用正则表达式，匹配包含“a” 的所有内容
print(t_list)

print('-'*80)

# 用方法来搜索：传入一个函数，根据函数的要求来搜索
def name_is_exists(tag):         # 定义一个函数，传入一个标签tag
    return tag.has_attr("name")    # 检查所传入的标签是否含有name这个属性，有的话用return返回
t_list = bs.find_all(name_is_exists)
for item in t_list:   # 让打印结果以列表的形式输出，看起来更直观
    # print(t_list)
    print(item)

print('-'*80)

# (2)kwargs   参数
# t_list = bs.find_all(id = "head")
# t_list = bs.find_all(class_=True)
t_list = bs.find_all(href="http://news.baidu.com")
for item in t_list:
    print(item)

print('-'*80)

# (3) text参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
t_list = bs.find_all(text=re.compile("\d"))  # 利用正则表达式来查找包含特定文本的内容
for item in t_list:
    print(item)

print('-'*80)

# (4).limit 参数
t_list = bs.find_all("a",limit=3)  # limit 限制选择多少条数据
for item in t_list:
    print(item)

print('-'*80)

# css选择器
# t_list = bs.select("title")   # 通过标签来查找
# t_list = bs.select(".mnav")   # 通过类名来查找   .表示类，mnav表示类名
# t_list = bs.select("#u1")   # 通过id来查找   用法： #+id
# t_list = bs.select("a[class = 'bri']")   # 通过属性来查找   用法： a[]里边的属性
t_list = bs.select("head > title")   # 通过子标签来查找   用法：用 > 符号一层一层向下找
for item in t_list:
    print(item)

print('-'*80)

t_list = bs.select(".mnav ~ .bri")   # 通过兄弟标签来查找  用法：用 ~ 符号连接其兄弟标签
print(t_list[0].get_text())   # 通过获取列表第一个元素，然后用.get_text()方法获取文本内容
