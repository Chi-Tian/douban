# -*- coding = utf-8 -*-
# @Time : 2020/10/11 11:42
# @Author : TianChi
# @File : testRe.py
# @Software : PyCharm

# 正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re
# 创建模式对象，用compile
pat = re.compile("AA")   # 此处的AA是正则表达式，用来去校验其他的字符串
# m = pat.search("CBA")    # search字符串是指被校验的内容， 用search方法，进行比对查找
# m = pat.search("ABCAA")    # search字符串是指被校验的内容   # <re.Match object; span=(3, 5), match='AA'>
m = pat.search("AABCAABBAAA") # search字符串是指被校验的内容   # <re.Match object; span=(0, 2), match='AA'>
print(m)                      # search 只能匹配到第一个符合条件的位置

print("-" * 60)

# 没有创建模式对象
m = re.search("asd","Aasd")   # 前边的字符串是规则（模板），后边的字符串是校验的对象
print(m)

print("-" * 60)

print(re.findall("a","ASDaDFGAa"))   # 前边的字符串是规则（正则表达式），后边的字符串是被校验的字符串  # ['a', 'a']
print(re.findall("[A-Z]","ASDaDFGAa"))  # 前边的字符串是规则（正则表达式），后边的字符串是被校验的字符串  # ['A', 'S', 'D', 'D', 'F', 'G', 'A']
print(re.findall("[A-Z]+","ASDaDFGAa"))  # 前边的字符串是规则（正则表达式），后边的字符串是被校验的字符串  # ['ASD', 'DFGA']

print("-" * 60)

# sub
print(re.sub("a","A","aascdcasd"))    # sub()有三个参数，找到a用A来替换，返回替换后的字符串

print("-" * 60)

# 建议在正则表达式中，被比较的字符串前面加上r，就不用担心转义字符的问题了
a = r"\aabdsd-\'"
print(a)
