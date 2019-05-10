# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 16:43

### Python中的集合类型:
# 列表(list): list = []   ---> 有先后顺序,有下标,元素可重复,可变类型
# 元组(tuple): tuple = () ---> 有先后顺序,有下标,元素可重复,不可变类型(只能查询)
# 字典(dict): dict = {key:value}  ---> 没有先后顺序,没有下标,键值对形式,key不可重复,value可重复,可变类型
# 集合(set):  set = set()   ---> 没有先后顺序,没有下标,元素不可重复,可变类型

### 集合(set)中的方法:
# add() 添加一个元素
# copy() 拷贝集合
# pop() 删除一个元素
# remove() 删除指定的元素
# clear() 清除集合中的元素

s = {11,22,33,44}
s.add(55)
print(s)


### 使用set集合去除list列表中的重复元素
list = [11,22,88,44,11,55,22]
s2= set(list)
print(s2)

