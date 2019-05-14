# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-14 9:11

### 函数也是一个对象
def demo():
    print("print demo ...")

test = demo  # 此处函数后面没加小括号,是把函数赋值给一个变量,并不是在调用一个函数
test()  # demo ...
del demo
# demo() # 报错
test() # demo ...

### 在函数中定义函数,并从函数中返回函数
def demo2(name="python"):
    def func1():
        return "return func1 ..."
    def func2():
        return "return func2 ..."

    if name == "python":
        return func1
    else:
        return func2

run = demo2()  # 此处函数后面有加小括号,函数会被执行
print(run)  # <function demo2.<locals>.func1 at 0x0000000002734F28>

str = run()
print(str)  # func1 ...

### 将函数作为参数传递给另一个函数
def test1():
    return "return test1 ..."

def doTest1(func):
    print("print doTest1 ...")
    print(func())

doTest1(test1)