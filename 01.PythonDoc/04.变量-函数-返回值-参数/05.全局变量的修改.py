# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 在函数中修改全局变量:
# 1. 如果全局变量是可变类型,可以直接在函数中修改全局变量的值;如 列表,字典
# 2. 如果全局变量是不可变类型,不可以直接在函数中修改全局变量的值;如 字符串,数值
# - 在函数中加入 global 不可变类型全局变量名称 修改的值,本质上只是修改了全局变量的引用

# 可变类型:值可以修改(内存地址不变,值改变), 引用可以修改(变量的内存地址改变了)
# 不可变类型:值不可以修改,可以修改变量的引用(=赋值号)

# 全局变量定义在调用函数之前

names = ["zhangsan","lisi","wangwu"]
dict = {"name":"chendong"}
string = "chen"
num = 100

def test1():
    print("全局变量列表原始数据: %s"%names)
    names.append("liuliu")
    dict["age"] = 23
    string = "hello word"  # 此处并没有修改全局变量,只是在函数中定义了一个与全局变量名称相同的局部变量

def test2():
    global string
    string = "hello word"  # 此处修改全局变量,本质上只是改变了全局变量的引用
    global num
    num += 1

test1()
test2()
print("全局变量列表修改后数据: %s"%names)
print("全局变量字典修改后数据: %s"%dict)
print("全局变量字符串修改后数据: %s"%string)
print("全局变量数值修改后数据: %s"%num)