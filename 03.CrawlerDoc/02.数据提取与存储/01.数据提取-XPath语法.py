# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-27 9:28

# XPath语法与Lxml模块
# XPath : 是一门在XML和HTML文档中查找信息的语言,可以用来在XML和HTML文档中对元素及属性进行遍历

# XPath开发工具:
# 1. FireFox浏览器插件: Try XPath
# 2. Chrome浏览器插件: XPath Helper  ---> 快捷键开启:CTRL+SHIFT+X

# XPath语法: 选取节点(标签)
# /     根目录下查找           /title
# //    整个页面查找           //div
# @     某个节点属性           //div[@class="name"]
# text() 标签下的文本内容      /div/a/text()

# XPath语法: 谓语
# /bookstore/book[1]          选取bookstore下的第一个book元素
# /bookstore/book[last()]     选取bookstore下的最后一个book元素
# //book[@price]              选取拥有price属性的book元素

# XPath语法: 通配符
# *         匹配任意节点              //body/*        选取body节点下的所有子节点
# @*        匹配节点中的任何属性      //book[@*]      选取所有带有属性的book元素

# 安装: pip install lxml
from lxml import etree

htmlElement = etree.HTML("text")   # 参数为一个字符串
print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

htmlElement = etree.parse("text.html")  # 参数为一个html格式文件
print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

parse = etree.HTMLParse(encoding="utf-8")  # 解析参数
htmlElement = etree.parse("text.html", parse=parse)
print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

###########################示例如下##################################
import requests

url = "https://www.qidian.com/all?chanId=4&subCateId=12"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}

response = requests.get(url, headers=headers)
htmlElement = etree.HTML(response.text)  # 接受一个字符串参数,返回的是一个Element对象

names = htmlElement.xpath('//h4/a/text()')
authors = htmlElement.xpath('//p[@class="author"]/a[@class="name"]/text()')
# print(names)  # 列表数据
# print(authors)  # 列表数据

for name, author in zip(names, authors):
    print("书名: " + name, " ---> ", "作者: " + author)

for num in range(len(names)):
    print(names[num], " : ", authors[num])