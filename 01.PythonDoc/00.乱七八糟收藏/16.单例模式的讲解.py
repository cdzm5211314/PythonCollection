# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-24 13:55

### 单例模式方式一: __new__()
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

class Demo(Singleton):
    def __init__(self):
        print("Demo类的初始化方法...")

d1 = Demo()
d2 = Demo()
print(id(d1))  # 4903992
print(id(d2))  # 4903992

### 单例模式方式二: 模块方式(Python独有的)
# 注:Python模块加载只执行一次
## singleton.py
# class MySingleton(object):
#     def run(self):
#         print("MySingleton run ...")
# mySingle = MySingleton()

## main.py
# from singleton import mySingle
# from singleton import mySingle as single
# print(id(mySingle))
# print(id(single))

