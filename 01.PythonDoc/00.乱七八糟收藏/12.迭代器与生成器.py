# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-9-11 16:16

### 列表生成式
# print([i*2 for i in range(1,34)])
# print([i*2 for i in [2,3,5,8,7]])

### 生成器(generator):
# 创建生成器gerenator,有很多方法,最简单的一种方式只要把列表推导式的[]变成(),就是创建一个生成器
# generator = (i*2 for i in range(10))
# print(generator)  # <generator object <genexpr> at 0x0000000002537BA0>
# 依次遍历生成器中的数据
# for i in generator:
#     print(i)

# __next__() 方法只会记住当前的位置
# print(generator.__next__())

### 斐波那契数列: 1,1,2,3,5,8,13,21,34,......
# 除第一,第二个数之外,后面的任意一个数都是前两个数相加得到
# 求斐波那契数列的前N位是何值???
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n + 1
#     return "done"
# fib(10)

# 递归方式求斐波那契数列的第N位数是何值???
# def factorial(n):
#     if n == 1 or n == 2:
#         return 1
#     return factorial(n-1) + factorial(n-2)
# print(factorial(10))


### 可迭代对象:
## 直接作用于for 循环的数据类型有以下几种:
#   一类是集合数据类型:如list,tuple,dict,set,str
#   一类是generator,包括生成器和带yield的generator function
## 以上这种可以直接作用于for循环的对象统称为可迭代对象: Iterable
#   可以使用isinstance() 判断一个对象是否是Iterable对象
# from collections import Iterable
## 判断是否为可迭代对象Iterable
# print(isinstance([2,4,6,8],Iterable))  # 列表list
# print(isinstance((11,22,33),Iterable))  # 元组tuple
# print(isinstance({"name":"zhangsan","age":20},Iterable))  # 字典dict
# print(isinstance("你好",Iterable))  # 字符串str
# generator = (i*2 for i in range(10))
# print(isinstance(generator,Iterable))  # 生成器
# print(isinstance(100,Iterable))  # 数字:不是可迭代对象


### 迭代器:可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
#   可以使用isinstance() 判断一个对象是否是Iterator对象
from collections import Iterator
## 判断是否为迭代器对象Iterator
# print(isinstance([2,4,6,8],Iterator))  # 列表list
# print(isinstance((11,22,33),Iterator))  # 元组tuple
# print(isinstance({"name":"zhangsan","age":20},Iterator))  # 字典dict
# print(isinstance("你好",Iterator))  # 字符串str
# generator = (i*2 for i in range(10))
# print(isinstance(generator,Iterator))  # 生成器:是迭代器对象
# print(isinstance(100,Iterator))  # 数字


### 生成器都是Iterator迭代器对象,list,tuple,dict,set,str虽然是Iterable可迭代对象,但却不是Iterator迭代器对象
### 如果要把list,tuple,dict,set,str等Iterable可迭代对象变成Iterator迭代器对象,可以使用iter()函数
# 把以下Iterable可迭代对象变成Iterator迭代器对象
print(isinstance(iter([2,4,6,8]),Iterator))  # 列表list
print(isinstance(iter((11,22,33)),Iterator))  # 元组tuple
print(isinstance(iter({"name":"zhangsan","age":20}),Iterator))  # 字典dict
print(isinstance(iter("你好"),Iterator))  # 字符串str




