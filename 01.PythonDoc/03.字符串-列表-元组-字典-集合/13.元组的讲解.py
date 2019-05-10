# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 元组的讲解:元组有两个方法
# count()
# index()

# 元组跟列表很类型,唯一的区别在于元组的元素不能修改
# 注: 元组中只有一个元素时,后面需要加上一个逗号,

names = ("张三","李四","王五")
print(names)

# 根据元组的下标取出元素
print(names[1])

names[2] = "陈栋"
