# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 17:22

# is : 是比较两个引用是否指向同一个对象(引用比较)
# == : 是比较两个对象是否相等(值比较)

list1 = [11,33,55,77]
list2 = list1
list3 = list1[:]
print(list1 == list2)  # True
print(list1 is list2)  # True
print(list1 == list3)  # True
print(list1 is list3)  # False

############################

class Person(object):
    def __init__(self,name):
        self.name = name

p1 = Person("zhangsan")
p2 = Person("zhangsan")
p3 = p2
print(p1 == p2)  # False
print(p1 is p2)  # False
print(p3 == p2)  # True
print(p3 is p2)  # True
