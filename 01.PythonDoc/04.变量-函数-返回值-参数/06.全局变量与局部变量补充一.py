# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 全局变量与局部变量补充1

# 当全局变量是不可变类型时:即字符串 ,数据类型 ,元组
# 不能在函数中直接修改全局变量的值,如果需要修改需要在函数的第一行声明"global 全局变量名称"

a = 100

def test1():
    global a
    print("----------")
    a += 1
    print(a)

def test2():
    print("==========")
    print(a)
    
test1()
test2()   
    
    
    
    
