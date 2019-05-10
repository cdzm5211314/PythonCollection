# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:04

""""
* * * * *
 * * * *
  * * *
   * *
    *
"""

num = int(input("需要打印等边三角形: "))

x = 0
while x < num:  # 控制打印的行数;假设num=4,打印4行,x从0开始,num =3时是最后一次循环
    y = 0
    while y < x :  # 打印当前行前面的空格,第一行不打印空格,第二行1个空格...
        print(" ",end = "")
        y += 1
    z = num - x  # 打印*号,第一行打印4个*
    while z > 0:
        print("*",end = " ")
        z -= 1
    print()
    x += 1
