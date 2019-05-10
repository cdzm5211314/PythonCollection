# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 列表的嵌套

import random

aaa = ["aaa","bbb","ccc"]
bbb = ["AA","BB","CC"]
ccc = ["aA","bB","cC"]

list = []

list.append(aaa)
list.append(bbb)
list.append(ccc)

print(list)

# 循环遍历嵌套列表
for temps in list:
    for temp in temps:
        print(temp,end = " ")
    print("\n--------")
# 练习:一个学校有3个办公室,有8位老师,需要随便分配老师到这3个办公室中

offices = [[],[],[]]
teachers = ["张老师","李老师","王老师","陈老师","刘老师","徐老师","郑老师","吕老师"]


for teacher in teachers:
    # 随机数0 1 2--->表示办公室在列表offices中的下标
    index = random.randint(0,2)
    offices[index].append(teacher)
# print(offices)

# 输入每个办公室的老师信息
for office in offices:
    # 根据每个办公室获取老师信息
    for teacher in office:
        print(teacher,end = " ")
    print("\n=========")













