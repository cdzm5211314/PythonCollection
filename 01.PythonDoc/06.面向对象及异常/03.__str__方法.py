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
    def __str__(self):
        # 必须返回一个字符串
        return "我的小猫[%s]"% self.name

# tom 是全局变量
tom = Cat("Tom")
print(tom)

print("*" * 50)





