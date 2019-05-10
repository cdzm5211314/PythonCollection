# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-28 15:51

# threading模块提供了哪些方法:
# threading.current_thread(): 返回当前的线程变量。
# threading.enumerate(): 返回正在运行的线程数的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.active_count(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

# Thread类提供了哪些方法:
# run():        用以表示线程活动的方法。
# start():      启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive():    返回线程是否活动的。
# getName():    返回线程名。
# setName():    设置线程名。

from threading import Thread
import threading
import time

def coding():
    for i in range(1,4):
        # print("正在写代码...%s"%i)  # 传统方式
        print("正在写代码...%s"%threading.current_thread())    # 多线程方式
        time.sleep(1)

def drawing():
    for i in range(1,4):
        # print("正在画画...%s"%i)  # 传统方式
        print("正在画画...%s"%threading.current_thread())    # 多线程方式
        time.sleep(1)

### 传统方式
def run_single():
    coding()
    drawing()

### 多线程的方式
def run_thread():
    # 创建两个线程
    t1 = Thread(target=coding)   # target传入一个函数名
    t2 = Thread(target=drawing)  # target传入一个函数名
    # 开启线程
    t1.start()
    t2.start()

    print(threading.enumerate())  # 查看运行的线程个数

if __name__ == '__main__':
    # run_single()
    run_thread()


#################################################################
# 创建线程的两种方式:
# 第一种方式: Thread(): target参数表示线程目标,args参数是一个元组
# def test():
#     for i in range(1,4):
#         print("线程+: %s"%i)
#         time.sleep(2)
# # 创建线程
# t1 = Thread(target = test,args=("1",))
# t2 = Thread(target = test,args=("2",))
# # 启动线程
# t1.start()
# t2.start()

# 第二种方式: 继承threading.Thread类,重写父类的run方法
# class MyThread(threading.Thread):
#     # 重复父类的run方法
#     def run(self):
#         for i in range(1,4):
#             print("线程*: %s"%i)
#             time.sleep(2)
# # 创建线程
# mt1 = MyThread()
# mt2 = MyThread()
# # 开启线程
# mt1.start()
# mt2.start()




