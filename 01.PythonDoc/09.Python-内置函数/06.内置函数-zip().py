# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-11-16 11:05

# zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

list1 = ["zhangsna","lisi","wangwu"]
list2 = ['a','b','c','d','e']

zz = zip(list1,list2)
print(zz)                # <zip object at 0x0000000002914148>
print(zip(list1,list2))  # <zip object at 0x0000000002914108>

for i in zz:
    print(i,type(i)) # ('zhangsna', 'a') <class 'tuple'>

for x,y in zip(list1,list2):
    print(x,y) # zhangsna a lisi b wangwu c
    # print(type(x),type(y),end=" ") # str

for a,b in zip(list2,list1):
    print(a,b) # a zhangsna b lisi c wangwu
    # print(type(a), type(b), end=" ")  # str
