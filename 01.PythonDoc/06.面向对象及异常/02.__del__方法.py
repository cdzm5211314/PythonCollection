# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 定义一个猫类
class Cat:
    """ 这个类文档"""
    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了..."% self.name)
    def __del__(self):
        print("%s 去了!!!"% self.name)

# tom 是全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除已个对象
del tom

print("*" * 50)
# 程序执行完成后会默认掉用__del__方法




