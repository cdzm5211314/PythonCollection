# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

names = ["zhangsan","lisi","wangwu","liuliu"]
nums = (111,222,333,444,555)

# 第一种迭代
j = 0
print("序号\t姓名")
for i in names:
    j += 1
    print("%d\t%s"%(j,i))
print("*"*10)

# 第二种迭代: enumerate 枚举,内置函数
for i,item in enumerate(names,1):
    print("%d\t%s"%(i,item))




