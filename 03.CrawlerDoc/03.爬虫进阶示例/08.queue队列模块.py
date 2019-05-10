# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-28 16:02

# Python中的queue模块: queue.Queue类
# Queue: FIFO先进先出
# LifoQueue: LIFO后进先出
# PriorityQueue: 优先级

# 队列对象方法: Queue(maxsize) - 创建一个先进先出的队列
# Queue.qsize()：    返回队列的大小
# Queue.empty():     判断队列是否为空,队列为空返回True
# Queue.full():      判断队列是否满了,队列满了返回True
# Queue.get(item, block=True, timeout=None): 从队列中取最后一个数据。
# Queue.put(item, block=True, timeout=None): 将数据放入队列中。
# Queue.join():      一直阻塞直到队列中的所有元素都被取出和执行

# Queue.put_nowait(item): 往队列里存放元素，不等待
# Queue.get_nowait(item): 从队列里取元素，不等待
# Queue.task_done()

from queue import Queue
import threading
import time

def set_value(qu):
    index = 0
    while True:
        qu.put(index)
        index += 1
        time.sleep(2)

def get_value(qu):
    while True:
        print(qu.get())

def main():
    qu = Queue(5)  # 创建空间为5的队列
    # 创建多线程
    t1 = threading.Thread(target=set_value,args=[qu])
    t2 = threading.Thread(target=get_value,args=[qu])
    # 开启线程
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()


