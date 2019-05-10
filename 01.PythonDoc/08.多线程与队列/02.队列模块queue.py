# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-12-19 11:07

# Python提供了一个队列操作:模块queue ---> 类Queue
# Queue: FIFO先入先出
# LifoQueue: FIFO后入先出
# PriorityQueue: 优先级

# 队列对象方法:
# Queue.empty(): 判断队列是否为空
# Queue.join() 一直阻塞直到队列中的所有元素都被取出和执行
# Queue.get(item, block=True, timeout=None): 从队列里取数据。
# Queue.put(item, block=True, timeout=None): 往队列里放数据。
# Queue.qsize() ：返回queue的近似值。注意：qsize > 0不保证(get)取元素不阻塞。qsize < maxsize不保证(put)存元素不会阻塞
# Queue.full(): 判断是否满了
# Queue.put_nowait(item): 往队列里存放元素，不等待
# Queue.get_nowait(item): 从队列里取元素，不等待
# Queue.task_done()




