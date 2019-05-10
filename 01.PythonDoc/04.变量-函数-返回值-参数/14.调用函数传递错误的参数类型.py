# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 定义函数求两个数的和
def sum(a,b):
    if not isinstance(a,(int,float)):
        print("传递的参数a是%s,不是数字类型"%a)
        # 如果a不是一个数字,函数后面的代码就没有必要执行了
        return
    elif not isinstance(b,(int,float)):
        print("传递的参数b是%s,不是数字类型"%b)
        # 如果a不是一个数字,函数后面的代码就没有必要执行了
        return
    sum = a + b
    return sum
sum = sum(7,"abc")
print(sum)