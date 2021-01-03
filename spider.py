# -*- coding = utf-8 -*-
# @Time : 2020/10/10 16:54
# @Author : TianChi
# @File : spider.py
# @Software : PyCharm

import re  # 正则表达式，进行文字匹配r
import urllib.error  # 指定URL，获取网页数据
import urllib.request
import xlwt  # 进行excel操作
from bs4 import BeautifulSoup  # 网页解析，获取数据


# 思路：
# 1.爬取网页
# 2.逐一解析数据
# 3.保存数据

def main():
    baseurl = 'https://movie.douban.com/top250?start=0'  # 基础网址
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = r'.\豆瓣电影Top250.xls'
    # 3.保存数据
    saveData(datalist, savepath)

    # askURL('https://movie.douban.com/top250?start=0')  # 调用askURL函数，将所爬取的网址参数加进去


# 影片详情的规则
find_link = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）
# ? 表示对前一个字符*扩展0次或1次，即后边可能有一个网站链接，也可能是空的，什么也没有
# 影片的图片规则
find_img = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在其中（因为.表示任一字符，除了换行符）
# 影片的片名规则
find_title = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片评价人数
find_judge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
find_inq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
find_bd = re.compile(r'<p class="">(.*?)</p>', re.S)  # re.S 让换行符包含在其中（因为.表示任一字符，除了换行符）


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 利用循环，每次爬取1页（25条），循环10次，将250条信息爬取下来  # range(0,10)表示从0到9，左闭右开
        url = baseurl + str(i * 25)  # i=0时，url从 0开始，i=1时，url=0+25=25，从第26个开始爬，每页25个，所以i=1时，从第2页开始爬，以此类推，i=9时，从第10页开始爬
        html = askURL(url)  # 调用askURL函数来获取网页内容，执行一次就表示获得一页，将获得一页存储到字符串html中
        # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")  # 利用html.paeser解析器，来解析html这个对象，将整个文档放在内存里，形成一个树形结构的对象
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串，形成列表
            # class 是一个类别，在这个里，class是div里边的一个属性，所以在class后边加一个_(下划线)
            # print(item)   # 为了测试：查看电影item的全部信息
            # break
            data = []  # 保存一部电影的所有信息
            item = str(item)  # 将item转型为字符串

            # 影片详情的链接
            link = re.findall(find_link, item)[0]  # re库用来通过正则表达式查找指定字符串   # find_link是正则表达式的规则，
            # 添加链接                                 # [0] : 分析这个网页的源码，发现存在相同的地址出现两次，所以只取第一次，用[0]
            data.append(link)  # 添加链接

            # 添加图片
            img_src = re.findall(find_img, item)[0]
            data.append(img_src)  # 添加图片

            # 添加电影名
            titles = re.findall(find_title, item)  # 片名可能只有一个中文名，没有外国名
            data.append(titles[0])  # 添加中文名
            if len(titles) == 2:
                data.append(titles[1].replace("/", ""))  # 添加外国名
            else:
                data.append(' ')  # 如果没有外国名，则外国名留空

            # 添加评分
            rating = re.findall(find_rating, item)[0]  # 添加评分
            data.append(rating)

            # 添加评价
            judge = re.findall(find_judge, item)[0]  # 添加评价
            data.append(judge)

            # 添加概述
            inq = re.findall(find_inq, item)  # 添加概述
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 如果没有概述，则概述留空

            # 添加电影相关内容
            bd = re.findall(find_bd, item)[0]
            bd = re.sub(r'<br(\s+)?/>(\s+)?', ' ', bd)
            # 去掉<br/>   sub()里边有三个参数，第一个是被替换掉内容，第二个是替换成什么，第三个是对谁（哪个变量里的内容）来进行替换
            bd = re.sub('/', ' ', bd)  # 替换 / 符号
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 将一部电影的信息加入到datalist中

            # print(link)
            # print(img_src)
            # print(titles)
            # print(rating)
            # print(judge)
            # print(inq)
            # print(bd)
    print(datalist)
    return datalist


# 爬取得到一个指定的URL的网页内容
# 这是实现爬取网页的具体代码
# askURL函数执行一次，就获取一页25条信息
def askURL(url):  # 定义一个请求URL的函数
    head = {  # 头部信息   模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge) Chrome/85.0.4183.121 Safari/537.36"
    }  # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器。（本质上是告诉浏览器我们可以接收什么水平的文件内容）
    request = urllib.request.Request(url, headers=head)  # 用这个方法向豆瓣服务器发消息，Request()的括号中封装了向服务器发送请求所需要的一些信息
    html = ""  # 访问的是网页，需要存储，我们定义一个字符串来存储所访问的网页
    try:  # 可能会发生一些问题，所以做一个异常处理
        response = urllib.request.urlopen(request)  # 发出请求，response来接收一个返回来的封装的对象
        html = response.read().decode('utf-8')  # 读取返回来的封装的对象的信息
        # print(html)   # 将网页的html源码打印出来

    except urllib.error.URLError as e:  # 捕获可能发生的像 404、418等异常
        if hasattr(e, "code"):  # hasattr 的作用就是检查一下错误信息 e 这个对象中有没有 code 这个属性，
            print(e.code)
        if hasattr(e, "reason"):  # hasattr 的作用就是检查一下 e 这个对象中有没有 reason 这个属性，
            print(e.reason)
    return html  # 返回html，要有返回值，一会调用askURL函数时才能将获取的一页信息传递给调用的地方


# 保存数据
def saveData(datalist, savepath):
    print('save....')
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建book对象     # style_compression=0  样式压缩效果
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表  # cell_overwrite_ok=True   每个单元格写入新的内容时可以覆盖
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外国名', '评论', '评分数', '概况', '相关信息')  # 对列进行操作
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 写入列名
    for i in range(0, 250):
        print("这是第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存数据表


if __name__ == '__main__':  # 当程序执行时
    # 调用函数
    main()
    print("爬取完毕！")
