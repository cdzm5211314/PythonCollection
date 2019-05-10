# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 12:26

### 练习:使用*号打印到三角形

x = 5  # 控制行数
while x <= 5 and x > 0:
    y = 1  # 控制每行打印*号个数
    while y <= x :
        print("*",end = "")
        y += 1
    print()
    x -= 1
