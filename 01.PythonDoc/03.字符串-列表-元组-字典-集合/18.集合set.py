# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 集合是无序的,不重复的
#   去重: 把一个列表变成集合,就去重了: set(list)
#   关系测试: 测试两组数据之间的交集,差集,并集等关系

# 花括号或者set()函数可以用来创建集合
# 注意，你必须使用set()创建一个空的集合，而不能用{}；后面这种写法创建一个空的字典

s = {x for x in 'abracadabra' if x not in 'abc'}
print(s)

names = ["zhangsan","lisi","wangwu"]
list1 = [2,4,1,5,9,3,2,5]
s1 = set(list1)
print(s1,type(s1))

s2 = {3,5,7,1,8}
print(s2,type(s2))

# 取两个集合的交集
# print(s1.intersection(s2))
# print(s1 & s2)

# 取两个集合的并集
# print(s1.union(s2))
# print(s1 | s2)

# 取两个集合的差集:前者集合里面有的,后者集合里面没有的
# print(s1.difference(s2))
# print(s1 - s2)  # 在前者集合中,不在后者集合中

s3 = {2,3,4}
# 子集,前者集合是否包含后者集合的子集
# print(s1.issubset(s2))
# print(s3.issubset(s1))
# 父集,前者集合是否是后者集合的父集
# print(s1.issuperset(s2))
# print(s1.issuperset(s3))

# 对称差集:取两个集合不相同的一部分
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)

print("*************************")

# 判断两个集合是否有交集,有交集返回False,没有交集返回True
# set1 = set([1,2,6])
# set2 = set([3,4,5])
# print(set1.isdisjoint(set2))

print("*************************")

# 给集合添加元素(添加一项)
# s1.add(10)
# 给集合添加元素(添加多项)
# s1.update([11,22,33])

# 删除集合的元素
# s1.remove(1)

# 集合的长度
# print(len(s1))

# 判断一个元素是否是集合的元素
# print( 2 in s1)

print(s1)



