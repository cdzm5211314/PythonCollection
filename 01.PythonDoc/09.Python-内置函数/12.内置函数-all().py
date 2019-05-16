# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-16 16:14

# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 True，如果是返回 True，否则返回 False。
# 元素除了是: 0、空、None、False 外都算 True。

# 语法: all(iterable)
# 参数: iterable ---> 元组或列表
# 返回值注意：空元组、空列表返回值为True，这里要特别注意。

name = ""
password = "123"

print(all((123,258)))        # True
print(all([name,password]))  # False
print(all([]))               # True

print(all([0]))         # False
print(all([""]))        # False
print(all([None]))      # False
print(all([False]))     # False

print(all(["None"]))    # True
print(all(["False"]))   # True

print(all("chen"))      # True



