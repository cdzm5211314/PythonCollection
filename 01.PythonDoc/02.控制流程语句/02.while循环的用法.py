# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 11:46

# while循环的格式:
# while 条件:
#     条件满足时,做的事情1...
#     条件满足时,做的事情2...
#     条件满足时,做的事情3...

### 练习:计算1-100的累积和
num = 1
sum = 0
while num <= 100 :
    sum += num
    num += 1
print("1-100的累积和: %d"%sum)


