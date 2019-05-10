# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 12:36

### break:(结束整个循环)只要在循环中执行到break,程序就终止,不在往下执行了
### continue:(结束本次循环,继续进行下一次循环)只要continue执行了,这次往下的代码统统不在执行

# break的用法案例:打印1-50的数字,当数字是20的时候结束循环
num = 1
while num <= 50:
    print("当前数字是: %d"%num)
    if num == 20:
        break
    num += 1

# contiune的用法案例:打印1-10之间是奇数的数字
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    else:
        print("1-10之间的奇数: %d"%x)
