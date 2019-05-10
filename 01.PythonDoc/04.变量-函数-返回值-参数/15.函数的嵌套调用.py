# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 函数的嵌套调用

# 定义函数与调用函数的顺序:调用函数语句不能出现在定义函数的前面
# 定义同名的函数:如果定义了两个相同的函数,只会保留最后的那个函数

# 定义函数
def test():
    print("---- test start -----")
    print("这里是test函数的执行代码...")
    print("---- test end -----")
# 定义函数
def testA():
    print("---- testA start -----")
    test()
    print("---- testA end -----")

# 调用函数
testA()

# 练习:函数的嵌套练习--->图形打印
# 1.自定义函数打印一条横线
# 2.打印自定义行数的横线

#自定义一个打印一个一行的*号
def printOneLine():
    print("*")  
    print("**")  
    print("***")  

def printMoreLine(num):
    i = 0
    while i < num:
        printOneLine()
        i += 1
    
#说明你要打印几条横线
line = int(input("请输入你要打印的行数:"))
printMoreLine(line)



