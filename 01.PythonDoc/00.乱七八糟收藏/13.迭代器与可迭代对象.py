# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 19:22
from collections import Iterable

# 迭代是访问集合元素的一种方式
# 迭代器是一个可以记住遍历的位置的对象,迭代器只能向前不能后退

# 可迭代对象:
    # 集合数据类型: 如 list tuple dict set str
    # 生成器和带 yield 的generator function

# 如何判断可迭代对象:
    # from collections import Iterable
    # isinstance([],Iterable)
print(isinstance([11,22,33],Iterable))

# 迭代器(Iterable):可以被next()函数调用并不断返回下一个值的对象称之迭代器
    # from collections import Iterable
    # isinstance((x for x in range(10)),Iterable)
    # iter()函数:将可迭代对象转换成迭代器
lists = [11,22,33]
it = iter(lists)
print(next(it))


