# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-28 17:29

import threading
import random
import time

gMoney = 1000  # 全局钱数
gCondition = threading.Condition()  # 定义锁
gTotalTimes = 10  # 生产者允许生产的次数
gTimes = 0 # 生产了多少次

# 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        global gTotalTimes
        while True:
            money = random.randint(100,1000)  # 随机产生100-1000的整数
            gCondition.acquire()
            if gTimes >= gTotalTimes:  # 生产次数大于允许的次数,不能再生产了
                gCondition.release()
                break
            gMoney += money
            gTimes += 1
            print("%s生产了%d元钱,剩余%d元钱..."%(threading.current_thread(),money,gMoney))
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.5)

# 消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)  # 随机产生100-1000的整数
            gCondition.acquire()
            while gMoney < money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print("%s准备消费%d,剩余%d钱,不够消费!!!" % (threading.current_thread(), money, gMoney))
                gCondition.wait()
            gMoney -= money
            print("%s消费了%d元钱,剩余%d元钱..."%(threading.current_thread(),money,gMoney))
            gCondition.release()
            time.sleep(0.5)

# 执行方法
def main():
    # 定义3个消费者
    for i in range(3):
        th = Consumer(name="消费者线程%d" % i)
        th.start()
    # 定义5个生产者
    for i in range(5):
        th = Producer(name="生产者线程%d"%i)
        th.start()

if __name__ == '__main__':
    main()


