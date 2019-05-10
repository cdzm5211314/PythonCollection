# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-03-30 15:13

# Series:系列数据,能够保存任何类型的数据(整数,字符串,浮点数,Python对象等)的一维标记数组,轴标签统称为索引.
# DataFrame:数据框,类似于数据库表结构的数据结构,其含有行索引和列索引,可以将DataFrame想成是由相同索引的Series组成的Dict类型.在其底层是通过二维以及一维的数据块实现.

import pandas

### 创建Series数据: 默认有一索引: 0 1 2 ...
# s = pandas.Series([5,3,7])
# print(s)
# 0    5
# 1    3
# 2    7
### 创建Series数据: 指定索引名称,索引名称个数与数组元素个数一致
# s = pandas.Series([5,3,7],index=['a','b','c'])
# print(s)
# a    5
# b    3
# c    7

### 创建DataFrame数据: 默认列,行都有索引: 0 1 2 ...
# d = pandas.DataFrame([[1,4,7],[2,5,8],[3,6,9],[0,10],["a","b","c","d"]])
# print(d)
#    0   1     2     3
# 0  1   4     7  None
# 1  2   5     8  None
# 2  3   6     9  None
# 3  0  10  None  None
# 4  a   b     c     d
# 列索引个数与二维数组中一维数组中的元素个数值最大值一致
# 行索引个数与二维数组的元素个数值一致

### 创建DataFrame数据: 指定索引名称
# 列索引个数与二维数组中一维数组中的元素个数值最大值一致,行索引个数与二维数组的元素个数值一致
# d = pandas.DataFrame([[1,4,7],[2,5,8],[3,6,9],[0,10],["a","b","c","d"]],columns=["one","two","three","four"])
# print(d)
#   one two three  four
# 0   1   4     7  None
# 1   2   5     8  None
# 2   3   6     9  None
# 3   0  10  None  None
# 4   a   b     c     d

### 创建DataFrame数据: 根据dict字典类型数据
# dict字典的key为列索引,dict字典key对应的value值为行数据
d = pandas.DataFrame({
    "one":4,
    "two":[3,6,9,],
    "three":list(str(258))
})
# print(d)
#    one  two three
# 0    4    3     2
# 1    4    6     5
# 2    4    9     8

### 数据框: head() 获取数据框中的头部数据,默认显示前5行,如果数据不够5行,全部取出来
# print(d.head())
#    one  two three
# 0    4    3     2
# 1    4    6     5
# 2    4    9     8
### 数据框: head() # 获取数据框中前2行的数据
# print(d.head(2))
#    one  two three
# # 0    4    3     2
# # 1    4    6     5
### 数据框: tail() 获取数据框中的尾部数据,默认显示后5行,如果数据不够5行,全部取出来
# print(d.tail(5))
#    one  two three
# 0    4    3     2
# 1    4    6     5
# 2    4    9     8
### 数据框: tail() 获取数据框中后2行的数据
# print(d.tail(2))
#    one  two three
# 1    4    6     5
# 2    4    9     8
### 数据框: describe() 按列统计数据框数据(统计数值列,不是数值列不统计)
# print(d.describe())
#        one  two
# count  3.0  3.0
# mean   4.0  6.0
# std    0.0  3.0
# min    4.0  3.0
# 25%    4.0  4.5
# 50%    4.0  6.0
# 75%    4.0  7.5
# max    4.0  9.0
"""
# count表示每列的元素个数
# menu表示每列的平均数
# std表示每列标准差
# min表示每列数据的最小值
# max表示每列数据的最大值
# 数值%表示每列的分位数
"""

### 数据框: T 转置(行变成列,列变成行)
print(d.T)
#        0  1  2
# one    4  4  4
# two    3  6  9
# three  2  5  8



