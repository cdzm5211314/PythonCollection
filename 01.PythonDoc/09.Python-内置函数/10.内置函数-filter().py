# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-13 17:01

# filter(): 过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表

number_list = range(-5, 5)
print(number_list)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))


