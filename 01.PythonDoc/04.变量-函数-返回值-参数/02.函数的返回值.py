# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 定义格式:
# def 函数名(参数):
#     return 返回结果

def testSum1(a,b):
    sum1 = a + b
    return sum1
# return 被执行后,不管后面还有什么代码,都不会再执行了

def testSum2(a,b):
    sum2 = a + b

# 当函数有返回值时,在调用这个函数的时候需要定义一个变量来接受这个返回值
s1 = testSum1(8,5)
print(s1)
# 当函数没有返回值时,在调用这个函数的时候却定义一个变量来接受,这时这个变量的值为None
s2 = testSum2(3,5)
print(s2)


