# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-04-02 19:35

# 数据变换: 目的是将数据转换为更方便分析的数据
# 简单变换: 通常使用函数转换的方式,如: 开方,平方,对数等

## 数据规范化:
# 离差标准化(最小-最大标准化): 消除量纲(单位)影响以及变异大小因素的影响
# x1 = (x - min) / (max - min)
# 即: (当前数据-最小值)/(最大值-最小值)
# 标准差标准化(零-均值标准化): 消除单位影响以及变量自身变异影响
# x1 = (x - 平均数) / 标准差
# 即: (当前数据-当前数据的平均数)/当前数据的标准差
# 小数定标标准化: 消除单位影响
# x1 = x / 10**(k)              # 10**k 表示10的k次方
# k = log10(x的绝对值的最大值)    #
# 即: 当前数据/10**(log10(当前数据的绝对值的最大值))

import pymysql
import pandas
import numpy

conn = pymysql.connect(host="127.0.0.1", user="root", passwd='root', db='pythondb')
sql = "select price,comment from taob"
data_sql = pandas.read_sql(sql, conn)
# print(data_sql)

# 离差标准化:
data1 = (data_sql - data_sql.min())/(data_sql.max() - data_sql.min())
# print(data1)

# 标准差标准化:
# print(data_sql.mean())  # 平均数
# print(data_sql.std())   # 标准差
data2 = (data_sql - data_sql.mean())/data_sql.std()
# print(data2)

# 小数定标标准化:
# print(data_sql.abs())           # 绝对值
# print(data_sql.abs().max())     # 绝对值中的最大值
# print(numpy.log10(5))           # 求以10为底,5的对数
# print(numpy.ceil(2.2))          # 小数进一取整,3
data3=data_sql/10**(numpy.ceil(numpy.log10(data_sql.abs().max())))
# print(data3)


## 数据离散化: 等宽离散化,等频率离散化,一维聚类离散化
# 示例: 对价格数据进行等宽离散化
data_price = data_sql[u'price'].copy()  # 复制价格的数据
# print(data_price,type(data_price))
data_price_t = data_price.T
price = data_price_t.values
# print(price)
# 等宽离散化,cut():第一个参数为数据,第二个参数表示分为几份,第三个参数labels表示标签
# 注: 划分几份,labels就有几个标签
k = 3  # 表示分为3份
data4 = pandas.cut(price,k,labels=["便宜","适中","贵"])
# print(data4)
k=[0,50,100,300,500,2000,price.max()]  # 划分6份:0-50,50-100,100-300,300-500,500-2000,2000-price.max()
data5 = pandas.cut(price,k,labels=["非常便宜","便宜","适中","有点贵","很贵","非常贵"])
# print(data5)


