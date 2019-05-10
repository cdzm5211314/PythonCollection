# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 18:49

### 在Python中,一边循环一边计算的机制称之为生成器:generator

x = [ i for i in range(5)]  # 这个一个推导式
y = ( i for i in range(5))  # 创建一个生成器对象
print(x)  # 列表
print(y)  # 生成器对象:<generator object <genexpr> at 0x000000000213FFC0>

# 可以通过next()函数获取生成器的下一个返回值
print(next(y))
print(next(y))

# 没有更多元素时抛出异常: StopIteration
# 生成器也可以使用for循环,生成器也是可迭代对象

print("*"*20)
# 获取斐波那契数列
def fib(times):
    n = 0
    a , b = 0 , 1
    while n < times:
        yield b
        a , b = b , a + b
        n = n + 1
    return "done"
gener = fib(8)
# next(gener)
for x in gener:
    print(x,end = " ")
