# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

"""
装饰器原则：
    不修改被修饰函数的源代码
    不修改被修饰函数的调用方式
装饰器实现：
    装饰器 = 高阶函数 + 函数嵌套 + 闭包
高阶函数定义：
    函数接受的参数是一个函数名
    函数的返回值是一个函数名
    满足上述提条件中的一个，都可以称为高阶函数
"""

import time
# 定义装饰器：功能 - 查看源程序函数demo的运行时间
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print("demo函数的运行时间：%s"%(stop_time - start_time))
        return res
    return wrapper

# 源程序代码函数demo
@timer
def demo():
    time.sleep(2)
    print("demo函数执行完毕...")
    return "源程序函数demo"

demo()