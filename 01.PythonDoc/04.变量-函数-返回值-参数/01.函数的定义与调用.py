# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 函数的定义格式:参数可有可没有
# def 函数名(参数1,参数2...):
#     pass代码...

### 定义函数时,函数的参数名称 称之为形参
### 定义的形参 不会 跟之前定义的变量有冲突
### 定义的形参 的作用范围只在定义的函数内部有作用

### 在调用函数,传递给函数的参数称之为 实参

# 定义函数:无参数
def printInfo():
    print("人生苦短,我要学Python...")
# 调用函数
printInfo()

# 定义函数:有参数
def area(r):
    s = 3.14 * (r**2)
    print("圆的的面积是: %s"%s)
# 调用函数,求圆的面积
area(4)

# 定义多参数函数: a 和 b 是形参
def testSum(a, b):
    sum = a + b
    print("两个数的和为: %d"%sum)
# 调用函数,求两个数的和
testSum(5,2)
