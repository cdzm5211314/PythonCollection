# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-03-30 17:31

# matplotlib模块: 用于作图,如: 折线图,散点图(plot),直方图(hist)

from matplotlib import pylab
import numpy

### 折线图/散点图(plot): x轴,y轴 注:x轴数据与y轴数据要一致
# 格式: plot(x轴数据,y轴数据,展现形式)
# 注: x轴数据与y轴数据要一致
## 设置颜色:
"""
# c - cyan - 青色
# r - red - 红色
# m - mangente - 品红
# g - green - 绿色
# b - blue - 蓝色
# y - yellow - 黄色
# k - black - 黑色
# w - white - 白色
"""
## 设置线条样式:
"""
# -     :直线
# --    :虚线
# -.    :一杠一点
# :     :细小虚线
"""
## 设置点样式:
"""
# s :方形
# h :六角形
# H :六角形
# * :星形
# + :加号形
# x :x形
# d :菱形
# D :菱形
# p :五角形
"""

# x = [1,2,3,4,8]         # x 轴
# y = [5,7,2,1,5]         # y 轴
# pylab.plot(x,y)         # 折线图
# pylab.plot(x,y,'k')     # 折线图,并设置折线颜色
# pylab.plot(x,y,'o')     # 散点图
# pylab.plot(x,y,'or')    # 散点图,并设置散点颜色
# pylab.plot(x,y,'--')    # 折线为虚线
# pylab.plot(x,y,'-.')    # 折线为一杠一点
# pylab.plot(x,y,'*')     # 散点为星形
# pylab.plot(x,y,'x')     # 散点为x形
# pylab.show()

# 示例: 为折线图/散点图添加标题,添加x轴名称,y轴名称
# x = [1,2,3,4,8]
# y = [5,7,2,1,5]
# pylab.plot(x,y)
# pylab.title("折线图")      # 添加标题
# pylab.xlabel("这是x轴")    # 添加x轴名称
# pylab.ylabel("这是y轴")    # 添加y轴名称
# pylab.xlim(0,20)          # 设置x轴范围
# pylab.ylim(2,10)          # 设置y轴范围
# pylab.show()

# 示例: 再一个图中设置几条折线图
# x1 = [1,2,3,4,8]
# y1 = [5,7,2,1,5]
# x2 = [3,6,7,9]
# y2 = [2,4,1,7]
# pylab.plot(x1,y1)
# pylab.plot(x2,y2)
# pylab.show()

# numpy模块随机数的生成
# 整数随机数据格式: numpy.random.random_integers(最小值,最大值,个数)
# 正态随机数据格式: numpy.random.normal(平均数,西格玛,个数)
import numpy
# data = numpy.random.random_integers(2,35,10)  # 生成整数随机数据
# print(data)  # [25 11 12 18 24 31 23 35 32 8]
# data = numpy.random.normal(5.0,2.0,5)         # 生成正态分布随机数据
# print(data)  # [ 1.72168167  4.68000836  3.76598832  5.709232   -0.50785851]

### 直方图(hist):
# 格式: hist(数据)
# import numpy
# data = numpy.random.normal(10.0,2.0,50)           # 使用正态随机数据
# data = numpy.random.random_integers(2,30,100)     # 使用常规随机数据
# pylab.hist(data)
# pylab.show()

# 示例: 设置直方图的宽度
# import numpy
# data = numpy.random.random_integers(2,30,100)      # 使用常规随机数据
# style = numpy.arange(2,19,4)     # x轴从2开始,间隔4格,17位4的倍数加+1
# pylab.hist(data,style)
# pylab.show()

# 示例: 子图,在一张图里绘制多个子图
# import numpy
# data = numpy.random.random_integers(2,30,100)      # 使用常规随机数据
# style = numpy.arange(0,19,2)     # x轴从2开始,间隔4格,17位4的倍数加+1
# pylab.subplot(2,3,5)             # 把一张图分成两行三列共六个区域,显示图在第五个区域
# pylab.hist(data,style)
# pylab.show()

# 示例: 子图,在一张图中显示三张子图,上面显示两张子图,下面显示一张子图,并在每个区域绘制直方图
import numpy
data = numpy.random.random_integers(2,30,100)      # 使用常规随机数据
style = numpy.arange(0,19,2)     # 从2开始,间隔4格,17位4的倍数加+1
pylab.subplot(2,2,1)
pylab.hist(data,style)          # 在第一行的第一列绘制直方图
pylab.subplot(2,2,2)
x = [1,2,3,4,8]
y = [5,7,2,1,5]
pylab.plot(x,y)                 # 在第一行的第二列绘制折线图
pylab.subplot(2,1,2)
pylab.hist(data,style)          # 在第二行(就一列)绘制直方图
pylab.show()




