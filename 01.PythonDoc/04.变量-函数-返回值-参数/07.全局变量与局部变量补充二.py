# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 全局变量与局部变量补充2

# 当全局变量是可变类型时:即列表,字典
# 可以在函数中直接修改全局变量的值

# nums = [11,22,33,44]
info = {"name":"chendong","age":19}

def test1():
    print("----------")
#     nums.append(55)
#     print(nums)
    info["name"] = "张三"
    print(info)

def test2():
    print("==========")
#     print(nums)
    print(info)
    
test1()
test2()




