# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

import time
# 定义装饰器：功能 - 查看源程序函数demo的运行时间
# 为装饰器传递一个参数，只需要在最外层在创建一个函数,并返回一个函数名
def param(p_type = "param"):
    def timer(func):
        def wrapper(*args, **kwargs):
            print("装饰器参数：" %p_type )
            start_time = time.time()
            res = func(*args, **kwargs)
            stop_time = time.time()
            print("demo函数的运行时间：%s"%(stop_time - start_time))
            return res
        return wrapper
    return timer

# 源程序代码函数demo
@param(p_type = "param")
def demo():
    time.sleep(2)
    print("demo函数执行完毕...")
    return "源程序函数demo"

demo()