# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-03-30 20:05

import numpy
import pandas
from matplotlib import pylab
""".csv格式数据:
"1","时寒冰：想念鲁比（随笔）","http://shihanbingblog.blog.hexun.com/108385409_d.html","21","0"
"2","老时与书","http://shihanbingblog.blog.hexun.com/108369380_d.html","316","1"
"3","私密写真集，看后请删除（仅限量发售铁杆订户）","http://shihanbingblog.blog.hexun.com/108367966_d.html","212","0"
"4","时寒冰：私密写真集，看后请删除（仅限量发售铁杆订户）","http://shihanbingblog.blog.hexun.com/108366125_d.html","747","1"
"5","特朗普一蠢全球股市就大涨","http://shihanbingblog.blog.hexun.com/108351141_d.html","4661","16"
"6","时寒冰：为何特朗普一蠢全球股市就大涨","http://shihanbingblog.blog.hexun.com/108346867_d.html","96","0"
"7","特朗普一蠢全球股市就大涨","http://shihanbingblog.blog.hexun.com/108346508_d.html","56","0"
"8","剖析楼市真相与趋势（万字长文）","http://shihanbingblog.blog.hexun.com/108282776_d.html","3054","4"
"9","第五次产业大转移与未来30年国运","http://shihanbingblog.blog.hexun.com/108282774_d.html","294","0"
"""
hexun_csv = pandas.read_csv("hexun.csv")
# print(hexun_csv.shape)          # 查看数据有多少行多少列
print(hexun_csv.values)         # 得到二维数组类型的数据:[[第一行数据],[第二行数据],...,[最后一行数据]]
# print(len(hexun_csv.values))    # len得到数据有多少条
# print(len(hexun_csv.values[2])) # len得到第二行数据有多少元素
# values[第几行][第几列]
# print(hexun_csv.values[3][2])   # 获取第三行第二列数据

# 想得到所有数据的评论数,因原数据所有评论数是在一列上,所以可以使用T转置数据,把评论数变成一行数据
data = hexun_csv.T
# print(data)   # 转置后的数据,行变成列,列变成行
x = data.values[3]  # 获取所有的评论数,设置为x轴
y = data.values[4]  # 获取所有的阅读数,设置为y轴
# print(x)
# print(y)

# 绘制折线图:
# pylab.plot(x,y)
# pylab.show()

# 绘制直方图: 两行一列,评论数与阅读数各占一个子图
# pylab.subplot(2,1,1)
# pylab.hist(x)
# pylab.subplot(2,1,2)
# pylab.hist(y)
# pylab.show()


