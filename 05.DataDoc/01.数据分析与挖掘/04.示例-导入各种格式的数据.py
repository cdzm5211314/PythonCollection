# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-03-30 16:18

import pandas

### 导入csv[.csv]文件格式数据:
"""csv格式:
"1","时寒冰：想念鲁比（随笔）","http://shihanbingblog.blog.hexun.com/108385409_d.html","21","0"
"2","老时与书","http://shihanbingblog.blog.hexun.com/108369380_d.html","316","1"
"3","私密写真集，看后请删除（仅限量发售铁杆订户）","http://shihanbingblog.blog.hexun.com/108367966_d.html","212","0"
"4","时寒冰：私密写真集，看后请删除（仅限量发售铁杆订户）","http://shihanbingblog.blog.hexun.com/108366125_d.html","747","1"
"5","特朗普一蠢全球股市就大涨","http://shihanbingblog.blog.hexun.com/108351141_d.html","4661","16"
"""
### 读取到.csv文件中的数据
data_csv = pandas.read_csv("hexun.csv")
# print(data_csv)
#          1                    时寒冰：想念鲁比（随笔）  ...    21   0
# 0        2                            老时与书  ...   316   1
# 1        3          私密写真集，看后请删除（仅限量发售铁杆订户）  ...   212   0
# 2        4      时寒冰：私密写真集，看后请删除（仅限量发售铁杆订户）  ...   747   1
# ...
### 统计读取到的.csv文件中的数据
# print(data_csv.describe())
#                  1            21            0
# count  5696.000000   5696.000000  5696.000000
# mean   2849.500000    772.570751     4.636236
# std    1644.437898   2814.228154    19.843046
# min       2.000000      1.000000     0.000000
# 25%    1425.750000      1.000000     0.000000
# 50%    2849.500000      2.000000     0.000000
# 75%    4273.250000    110.250000     0.000000
# max    5697.000000  62861.000000   363.000000

### 按照某列对读取到的.csv文件中的数据进行排序
# data_csv_sort = data_csv.sort_values(by="21")  # by="列名"
# print(data_csv_sort)

### 导入excel[.xls]文件格式数据:
"""excel格式:
id	阅读数
22	 8287
223	 323
8821 133
"""
### 读取到excel[.xls]文件中的数据
# data_excel = pandas.read_excel("abc.xls")
# 报错:ImportError: Install xlrd >= 1.0.0 for Excel support  需要安装库: pip install xlrd
# print(data_excel)
#     id   阅读数
# 0    22  8287
# 1   223   323
# 2  8821   133

### 导入MySQL数据库里的数据:
# 安装pymysql模块: pip install pymysql
import pymysql
# 链接mysql数据库
conn = pymysql.connect(host="localhost",user="root",passwd="root",db="sshxml")
sqlquery = "select * from book"
### 读取到mysql数据库中的数据
data_sql = pandas.read_sql(sqlquery,conn)
# print(data_sql)
#    id        name  price
# 0   1        java  120.0
# 1   2      python   95.0
# 2   3         php   60.0
# 取出某一列的值
# print(data_sql["price"],type(data_sql["price"]))
# 取出某一列的值中所有price是60.0的数据
# print(data_sql[data_sql["price"]==60.0],type(data_sql["price"]))
# print(data_sql["price"][data_sql["price"]==60.0],type(data_sql["price"]))
# 判断数据中是否有price是60.0的数据,有返回True,无返回False
# print(data_sql["price"]==60.0,type(data_sql["price"]))

### 导入html[.html]文件中的数据: <table></table>
# 安装html5lib模块: pip install html5lib
# 安装beautifulsoup4模块: pip install beautifulsoup4
"""html格式:
<html>
	html文件table表格数据
<table>
	<tr><td>7</td><td>9</td></tr>
	<tr><td>5</td><td>8</td></tr>
	<tr><td>2</td><td>6</td></tr>
</table>
</html>
"""
### 读取到html网页表格中的数据: <table></table>
data_html = pandas.read_html("abc.html")  # 从.html文件中读取表格数据
# data_html = pandas.read_html("https://book.douban.com/")  # 从网页中读取表格数据
# print(data_html)

### 导入文本[.txt]文件中的数据:
"""文本格式:
id 文章 阅读数
1 三八十年 2000
2 就手机卡 8299
3 卡激活卡回家啊 992
"""
### 读取到.txt文件中的文本数据:
# data_txt = pandas.read_table("abc.txt")
# print(data_txt)
