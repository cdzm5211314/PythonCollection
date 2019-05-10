# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-12-19 10:56

# Python提供了一个线程操作:模块threading ---> 类Thread

# threading模块提供了哪些方法:
    #threading.current_thread(): 返回当前的线程变量。
    #threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    #threading.active_count(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

# Thread类提供了哪些方法:
    # run(): 用以表示线程活动的方法。
    # start():启动线程活动。
    # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    # isAlive(): 返回线程是否活动的。
    # getName(): 返回线程名。
    # setName(): 设置线程名。

import threading
import time

# 创建线程的两种方式:
# 第一种
def test(num):
    print("线程: " + num)
    time.sleep(2)
# Thread(): target参数表示线程目标
# Thread(): args参数是一个元组
t1 = threading.Thread(target = test,args=("1",))
t2 = threading.Thread(target = test,args=("2",))
# 启动线程
t1.start()
t2.start()

# 第二种
class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__()
        self.num = num
    # 重复父类的run方法
    def run(self):
        print("线程: " + self.num)
        time.sleep(2)
# 创建线程
mt1 = MyThread("3")
mt2 = MyThread("4")
# 开启线程
mt1.start()
mt2.start()






