# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-04 9:42
import itertools
import time

# 排列:从n个不同元素中每次取出m（1≤m≤n）个不同元素，排成一列，称为从n个元素中取出m个元素的无重复排列或直线排列
# 从n个不同元素中取出m个不同元素的所有不同排列的个数称为排列种数或称排列数，
# pn = n * (n-1) * (n-2) ... 3 * 2 * 1 = n!

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# li2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# 排列,不重复
# for temp in list(itertools.permutations([1,2,3,4,5],3)):
#     time.sleep(1)
#     print(temp)
# mylist = list(itertools.permutations([1,2,3,4,5],3))
# print(len(mylist))
# print(mylist)

# 组合,不重复
# for temp in list(itertools.combinations([1,2,3,4,5,6,7,8,9,10],6)):
#     time.sleep(1)
#     print(temp)
# mylist = list(itertools.combinations([1,2,3,4,5,6,7,8,9,10],6))
mylist = list(itertools.combinations(li1, 6))
print(len(mylist))

print(mylist)

# 排列组合,可重复
# mylist = list(itertools.product([1,2,3,4,5,6,],repeat=4))
# # mylist = list(itertools.product("123456",repeat=4))
# print(len(mylist))
# print(mylist)

# 递归函数:求阶乘 n!
# def test(n):
#     if n == 1:
#         return 1
#     return n * test(n-1)
# print(test(33))
