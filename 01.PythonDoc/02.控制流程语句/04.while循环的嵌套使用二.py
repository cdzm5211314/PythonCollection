# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 12:09

### 练习:九九乘法表
x = 1  # 控制行数
while x <= 9:
    y = 1  # 控制行的列数
    while y <= x:
        # print(str(y) + "*" + str(x) + "=" + str(y*x),end = " ")
        print("%d*%d=%d\t"%(y,x,x*y),end = "")
        y += 1
    print()
    x += 1




