# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-28 17:07

import threading

VALUE = 0
gLock = threading.Lock()  # 多线程锁机制
def add_value():
    global VALUE  # 申明全局变量
    gLock.acquire()  # 加锁
    for i in  range(10000):
        VALUE += 1
        # print("VALUE = %s"%VALUE)
    gLock.release()  # 释放锁
    print("VALUE = %s" % VALUE)

def get_thread():
    for i in range(3): # 0 1 2
        th = threading.Thread(target=add_value)  # 创建多线程
        th.start()  # 启动多线程

if __name__ == '__main__':
    get_thread()


