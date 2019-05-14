# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-13 16:58

# map(): 会将一个函数映射到一个输入列表的所有元素上
# 语法: map(function_to_apply, list_of_inputs)

items1 = [1, 2, 3, 4, 5]
squared1 = []
for i in items1:
    squared1.append(i**2)
print(squared1)

items2 = [1, 2, 3, 4, 5]
squared2 = list(map(lambda x: x**2, items2))
print(squared2)
