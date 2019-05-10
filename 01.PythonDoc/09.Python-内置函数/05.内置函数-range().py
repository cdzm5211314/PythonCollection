# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-11-16 10:38

# range函数的原型： range(start, end, scan)
# 参数解析：
    # start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）; 输出: 0 1 2 3 4
    # end:计数到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5（俗称：包前不包后）
    # scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

print(range(5)) # range(0, 5)

for i in range(5):
    print(i,end=" ")  # 0 1 2 3 4

for i in range(1,6):
    print(i,end=" ")  # 1 2 3 4 5

for i in range(1,6,2):
    print(i,end=" ")  # 1 3 5