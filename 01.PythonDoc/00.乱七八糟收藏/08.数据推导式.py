# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 16:10

### range(1,10) 获取一个包头不包尾的范围对象

### 生成一个1-9的数字列表
list1 = [i for i in range(1,10)]
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

### 生成一个1-9的数字平方的列表
list2 = [ i**2 for i in range(1,10)]
print(list2) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

list3 = [x for x in range(1,3) for y in range(0,2)]
print(list3) # [1, 1, 2, 2]

list4 = [(x,y) for x in range(1,3) for y in range(0,2)]
print(list4) # [(1, 0), (1, 1), (2, 0), (2, 1)]

### 使用推导式取出1-100之间的所有奇数
list5 = [x for x in range(1,101) if x % 2 == 1]
print(list5)

### 使用推导式生成一个[[1,2,3],[4,5,6]...]的列表最大值在100以内
list6 = [ [1+i,2+i,3+i] for i in range(0,98) if i % 3 == 0]
print(list6)






