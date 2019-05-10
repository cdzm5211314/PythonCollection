# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 函数的嵌套练习

#函数的嵌套练习:求三个数的平均值

#自定义求三个数的和
def sumSan(a,b,c):
    sum = a + b + c
    return sum

#自定义求三个数的平均值
# def sumAvg(x,y,z):
#     sum = x + y + z
#     avg = sum / 3
#     return avg

def sumAvg(x,y,z):
    sum = sumSan(x,y,z)
    avg = sum / 3
    return avg

result1 = sumSan(11, 22, 33)
print("三个数的和为:%d"%result1)

result2 = sumAvg(111, 222, 333)
print("三个数的和的平均值为:%d"%result2)




