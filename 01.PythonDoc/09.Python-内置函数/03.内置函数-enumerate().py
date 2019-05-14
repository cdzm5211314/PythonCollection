# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-11-16 11:02

# 当遍历一个序列时，使用enumerate()函数可以同时得到位置索引和对应的值

for i, v in enumerate(['tic', 'tac', 'toe']): # 默认从0开始枚举
    print(i, v)

list = ["zhangsan","lisi",[2.4,6],8,"wangwu"]  # 默认从0开始枚举
for k,v in enumerate(list):
    print(k,v)

for i,value in enumerate(list,1):  # 从哪个数字开始枚举
    print(i,value)

