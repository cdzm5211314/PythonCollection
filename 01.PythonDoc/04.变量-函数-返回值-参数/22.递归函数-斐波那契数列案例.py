# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 练习:斐波那契数列案例 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..., n
# F(n)=F(n-1)+F(n-2)

def test(n):
    if n == 1 or n == 2:
        return 1
    return test( n - 1) + test( n - 2)
print(test(19))

# 获取斐波那契数列
num = []
for i in range(1,20):
    num.append(test(i))
print(num)

# 斐波那契序列
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b