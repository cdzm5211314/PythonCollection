# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-25 18:58

age = int(input("请输入你的年龄: "))
sex = input("请输入你的性别: ")

# and 表示并且, or 表示或者, not 表示不满足后面的条件
if age >= 18 and sex == "男":
    print("你可以外出工作了!!!")
elif age < 18 or sex == "女":
    print("你还不能出去工作...")
else:
    print("......")


