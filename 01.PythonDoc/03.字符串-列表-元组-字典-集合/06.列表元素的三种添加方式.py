# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 列表元素的三种添加方法

names = ["zhangsan","lisi","wangwu","liuliu","zhaoqi","chenba"]
# for循环遍历列表
for name in names:
    print(name,end=" ")
print("\n")

# append():在列表末尾处添加元素
names.append("lijiu")
print(names)

# 使用input动态添加名字元素到列表中
temp = input("请输入姓名:")
names.append(temp)
print(names)

# append():嵌套使用--->在一个列表元素中添加另一个列表
xxx = ["a","b","c"]
yyy = ["A","B","C"]
print(xxx)
print(yyy)
xxx.append(yyy)
print(xxx)
print(yyy)

print("-----append()讲解完毕-----")

# insert():在指定位置前插入一个元素
list1 = [11,33,55,88,77,66,44]
print(list1)

list1.insert(2, 123)
print(list1)

print("-----insert()讲解完毕-----")

# extend():将一个列表中的元素逐一添加到另一个列表中
aaa = [111,333,555,777,999]
bbb = [22,44,66,88]

print(aaa)
print(bbb)

aaa.extend(bbb)
print(aaa)
print(bbb)

print("-----extend()讲解完毕-----")



