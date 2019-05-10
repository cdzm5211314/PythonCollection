# -*- coding: utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-20 16:31

try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数: "))
    # 使用8除以输入的整数,并且输出
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确的整数...")


try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数: "))
    # 使用8除以输入的整数,并且输出
    result = 8 / num
    print(result)
except (ZeroDivisionError,ValueError):
    print("除0错误")
    print("请输入正确的整数...")


