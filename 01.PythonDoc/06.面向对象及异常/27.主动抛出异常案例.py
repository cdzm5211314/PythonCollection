# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# Python中提供了一个 Exception 异常类
# 在开发时,如果满足特定的需求,希望抛出异常,可以:
# 1. 创建一个 Exception 类的对象
# 2. 使用 raise 关键字抛出异常

### 需求:
# 定义 input_password 函数,提示用户输入密码
# 如果输入的密码 长度 < 8 ,则抛出异常
# 如果输入的密码 长度 >= 8 , 则返回输入的密码

def input_password():
    # 提示用户输入密码
    pwd = input("请输入你的密码: ")
    # 判断密码长度 >= 8 ,返回用户的密码
    if len(pwd) >= 8:
        return pwd
    # 判断密码长度 < 8 , 抛出异常
    # 创建异常对象,可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够...")
    # 主动抛出异常
    raise ex

try:
    print(input_password())
except Exception as  result:
    print(result)