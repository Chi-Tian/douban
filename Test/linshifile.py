# -*- coding = utf-8 -*-
# @Time : 2020/10/12 11:36
# @Author : TianChi
# @File : linshifile.py
# @Software : PyCharm

# age = 10
# print('我的年龄是%d岁'%age)
#
# age += 1
# print('我的年龄是%d岁'%age)
#
# age = 18
# name = 'xiaohua'
# print('我的名字是%s，我今年%d岁了'%(name,age))
#
#
# print('123456--------')
# print('123456\n--------')

# password = input('你的密码：')
# print('你输入的密码是:',password)
#
# password = input('请输入你的密码：')
# print('你输入的密码是:',password)




# age = 56
# print('----------if判断开始-----------')
# if age <= 18:
#     print('你还未成年')
# elif 18 <= age <=30:
#     print('你已经成年了，且你是青年人')
# else:
#     print('你已经老了')


# xingbie = 1
# danshen = 2
# if xingbie == 1:
#     print('是男生')
#     if danshen == 1:
#         print('我给你介绍一个吧')
#     else:
#         print('你给我介绍一个吧')
# else:
#     print('你是女生')
#     print('无语。。。。。。')


# import random
# computer = random.randint(1,5)
# print(computer)


# print('-'*20 + '欢迎来到猜拳游戏' + '-'*20)
# a= input('请输入：剪刀（0）、石头（1）、布（2）：')
# r = random.randint(0,2)
# print('产生的随机数为：',r)
# if a==r:
#     print('平局')
# elif a==0&r==2 or a== 1&r==0 or a==2&r==1:
#     print('你赢了')
# else:
#     print('你输了')

# name = 'beijing'
# for i in name:
#     print(i,end='')


#
# i = 1
# while i<5:
#     print('这是第%d次循环,i=%d'%(i,i))
#     i += 1


# i = 1
# sum = 0
# while i <= 100:
#     if i%2==0:
#         sum += i
#     i += 1
# print(sum)



# sum = 0
# for i in range(1,101):
#     if i%2 == 0:
#         sum += i
#         i += 1
# print(sum)


# i = 0
# while i < 10:
#     i += 1
#     print('i=%d'%i)
#     if i == 5:
#         continue
#     print(i)



# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d '%(i,j,i*j),end='')
#     print()


# i = 1
# while i <= 9:
#     j = 1
#     while j < i+1:
#         print('%d*%d=%d '%(i,j,i*j),end='')
#         j += 1
#     i += 1
#     print()

# my_str = 'I\'m a student'
# print(my_str)

# my_str = "Tony said \"i love you \""
# print(my_str)
#
# a = "https://www.baidu\\none"
# print(a)


# str = 'chengdu'
#
# # print(type(str))
# # print(str[1:4])
# # print(str[0:-1])
# # print(str*3)
# # print('xuzf' + str(123))
# print('hello\nchengdu')
# print(r'hello\nchengdu')

# bytes.decode(encoding='utf-8',errors='strict')

namelist = ['小明','小红','小张','小李','a','b','c','小明','4','1','2']
testlist = ['xiaomig','小红',123]
# print(namelist[3])
# print(namelist[1:5:3])  # 步长
# for name in namelist:
#     print(name)
# namelist.extend(testlist)
# print(namelist)
# namelist.insert(1,3)
# print(namelist)
# del namelist[2]
# print(namelist)
# namelist[2] = '小小张'
# print('小张' in namelist)
# print(namelist)
# namelist.append('xiaohong')
# print(namelist)

# list3 = namelist + testlist
# print(list3)
# namelist.sort()
# print(namelist)
# namelist.reverse()
# print(namelist)



# import random
# names = ['A','B','C','D','E','F','G','H']
# offices = [[],[],[]]
#
# # a = random.randint(0,2)
# # print(a)
# # for i in range(1,4):
# #     officenumber = random.randint(1,3)
# #     print('办公室号为%d'%officenumber)
# #
# #     print(i)
# # 将8个人随机分配到三个办公室
# i = 0
# for name in names:
#     index = random.randint(0,2)
#     # print(index)
#     offices[index].append(name)
#     # print(offices)
#
# i = 1
# for office in offices:
#     print('办公室%d的人数为：%d'%(i,len(office)))
#     i += 1
#     for name in office:
#         print('%s'%name,end='')
#     print('\n')


# tuple = (50)
# print(type(tuple))

# tuple = (50,)
# print(type(tuple))

# tuple1 = ('Google','baidu',2000,2020)
# tuple2 = (1,2,3,4,5,6,7)
#
# # print('tuple1[0]:',tuple1[2])
# print(tuple2[1:5])
# print(tuple2[0:6:2])

tuple1 = (12,34,56)
tuple2 = ('abc','xyz')
# tuple1[0] = 123 # 元组中的元素不能修改
# tup3 = tuple1 + tuple2
# print(tup3)
# del tuple1
# print('删除后的元组：')
# print(tuple1)
# for i in tuple1:
#     print(i)
# print(12 in tuple1)
# print(tuple1.count(12))


dict1 = {'name':'吴彦祖','age':'18'}
dict2 = {'sex':'男','heigh':'182'}
# print(dict['hah'])
# sex = dict.get('sex')
# print(age)
# print(type(sex))
# sex = dict.get('sex','男')
# print(sex)

# for key in dict:
#     print(key,dict[key])
# for key,val in dict.items():
#     print(key,val)
# print(dict.keys())
# print(dict.values())

# dict1['小李'] = 2005
# print(dict)
# del dict['name']
# print(dict)
dict1.pop('age')
print(dict1)
# print('name' in dict)
# dict1.update(dict2)
# print(dict1)

# namelist = ['小明','小红','小张','小李','a','b','c','小明','4','1','2']
# testlist = ['xiaomig','小红',123]
#
# # a = dict(zip(namelist,testlist))
# # print(a)
#
#
# s1 = set([4,2,1,3,3,2,4,3,1,5])
# s2 = set([2,2,2,5,5,6,6,6,4,5,2,2])
# print(s)
# for i in s:
#     print(i,end='')
# s1.update(s2)
# print(s1)
# s1.add('haha')
# s1.remove(1)
# print('弹出前为：%s'%s1)
# s1.pop()
# s1.pop()
# s1.pop()
# s1.clear()

