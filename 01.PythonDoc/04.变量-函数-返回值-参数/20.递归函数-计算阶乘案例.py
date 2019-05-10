# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 递归函数:
# - 在函数内部调用自己本身
# - 递归函数本质上是一个函数的循环调用,注意:有可能出现死循环
# - 一定要定义递归的边界(什么时候退出循环)

### 练习:计算阶乘 n! = 1 * 2 * 3 * 4 * 5 * ... * n
"""
1! = 1
2! = 2 * 1 = 2 * 1!
3! = 3 * 2 * 1 = 3 * 2!
4! = 4 * 3 * 2 * 1 = 4 * 3!
...
n! = n * (n-1)!
"""

# 第一种方法: while 循环
n = 4
result = 1
i = 1
while i <= n:
    result = result * i
    i += 1
print(result)

# 第二种方法: 递归函数
def test(n):
    if n == 1:
        return 1
    return n * test(n-1)
print(test(5))





