# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

def test1(x,y):
    x.replace("c","C")
    y.append(40)
    print("x变量指向的内存地址: %s" % id(x))
    print("y变量指向的内存地址: %s" % id(y))

a = "abcdef"
b = [10,20,30]
print("a变量指向的内存地址: %s"%id(a))
print("b变量指向的内存地址: %s"%id(b))
test1(a,b)


# 参数的引用传递

def test1(a):   # 这个a传递的是g_a的值的引用地址:即存放值100的地址
    a += 1      # 此时a的地址发生了变化,指向了存放值101的地址
    print(a)

def test2(a):
    a += a  # a+=a 是在源数据上进行修改
#     a = a + a # a=a+a 是先定义一个变量在修改
    print(a)

g_a = 100
test1(g_a)
print(g_a)


nums = [11,22,33]
test2(nums)
print(nums)