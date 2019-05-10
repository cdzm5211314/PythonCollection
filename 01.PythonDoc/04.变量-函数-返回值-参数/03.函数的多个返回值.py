# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 函数的多个返回值

# 如果一个函数有多个return 返回值,那么程序只要执行任何一个return
# 那么剩下的所有return 都不会被执行

# return 即是返回一个数据,又是只要被调用,就会立即结束当前的函数

def test():
    a = 100
    return a
    a = 200
    return a
    a = 300
    return a

# 返回多个值
def test2():
    name = input("请输入你的姓名:")
    myId = input("请输入你的id:")
    age = input("请输入你的年龄:")
#     return name,myId,age
    # 先把数据保存到元组中,然后在返回
#     info = (name,myId,age)
#     info = [name,myId,age]
    info = {"name":name,"id":myId,"age":age}
    return info
    

A = test()
print(A)

result = test2()
print(result)

