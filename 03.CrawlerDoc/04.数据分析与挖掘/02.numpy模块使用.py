# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-03-30 14:28

import numpy

# 创建一维数组格式: numpy.array([元素1,元素2,...,元素n])
# arr1 = numpy.array(["a","3","2","y"])
# print(arr1,type(arr1))  # ['a' 'z' '2' 'y'] <class 'numpy.ndarray'>
# print(arr1[2])  #  取出数组下标为2的数值(下标从0开始)

# 创建二维数组格式: numpy.array([元素1,元素2,...,元素n],[元素1,元素2,...,元素n],...,[元素1,元素2,...,元素n])
# arr2 = numpy.array([["a","2","y"],[2,5,7],[2,"s","3"]])
# print(arr2,type(arr2))
# print(arr2[0][1])  #  取出二维数中第1个数组中下标为1的数值(下标从0开始)


# 对数组中元素进行排序: sort() 默认从小到大排序
# arr1 = numpy.array(["a","3","2","y"])
# arr2 = numpy.array([["a","2","y"],[2,5,7],[2,"s","3"]])
# arr1.sort()
# print(arr1)  # ['2' '3' 'a' 'y']
# arr2.sort()
# print(arr2)  # [['2' 'a' 'y'],['2' '5' '7'],['2' '3' 's']]

# 取数组中元素的最大值与最小值:
# arr1 = numpy.array([3,1,5])
# arr2 = numpy.array([[3,6,9],[2,5,7],[1,4,7]])
# arr1_max = arr1.max()
# arr1_min = arr1.min()
# print(arr1_max,arr1_min)
# arr2_max = arr2.max()
# arr2_min = arr2.min()
# print(arr2_max,arr2_min)

# 数组切片: 按照下标取某一段的元素
# 格式:array[index:end]  --->  数组[起始下标:结束下标]
# 注: end > index
# 注: 如果index没有数值,表示从0开始取,如果end没有数值,表示取到最后一个
# 注: 如果end给定了数值,取得是起始下标位置到end-1下标位置的元素
arr1 = numpy.array(["a","3","2","y","bb","cc"])
arr2 = numpy.array([["a","2","y"],[2,5,7],[2,"s","3"],["c","z","5"]])
print(arr1[:2])  # 表示取下标0-1的元素,包头不包尾
print(arr1[1:])  # 表示取下标0-最后一个下标的元素
print(arr2[0:1])  # 表示取下标0-1的元素,包头不包尾
print(arr2[2:4])  # 表示取下标2-3的元素,包头不包尾

# numpy模块: 随机数据的生成
# 整数随机数据格式: numpy.random.random_integers(最小值,最大值,个数)
# 正态随机数据格式: numpy.random.normal(平均数,西格玛,个数)
import numpy
# data = numpy.random.random_integers(2,35,10)  # 生成整数随机数据
# print(data)  # [25 11 12 18 24 31 23 35 32 8]
# data = numpy.random.normal(5.0,2.0,5)         # 生成正态分布随机数据
# print(data)  # [ 1.72168167  4.68000836  3.76598832  5.709232   -0.50785851]


