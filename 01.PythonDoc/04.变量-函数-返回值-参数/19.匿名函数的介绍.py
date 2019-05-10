# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 匿名函数的定义格式:
# lambda [参数] : 表达式
# lambda函数接受任何数量的参数,但只能返回一个表达式的值
# 匿名函数不能调用print()函数,因为lambda需要一个表达式

def test(x,y):
    return x + y
print(test(2,3))

func = lambda a,b : a + b
print(func(2,3))

def test1(a,b,func):
    result = func(a,b)
    return result
print(test1(22,33,lambda x,y : x+y))

