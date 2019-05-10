# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 11:54

### 使用while循环嵌套打印一个矩形


y = 1  # y 表示矩形宽度
while y <= 6:  # 控制打印多少行
    x = 1  # x 表示矩形长度
    while x <= 10:  # 控制每行打印多少*号
        print("*",end = " ")  # print()函数默认是换行的,后面加上 end = "" 表示不换行
        x += 1
    print("")
    y += 1

