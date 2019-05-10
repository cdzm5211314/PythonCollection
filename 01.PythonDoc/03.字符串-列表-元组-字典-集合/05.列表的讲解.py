# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 列表讲解

# 列表的定义:存储多个数据,可以存储多种数据类型,也可以内建列表
namelist = ["zhangsan",19,"sex"]

# 注: 列表的切片操作,得到的还是一个列表

# 打印列表中的元素
print(namelist)

# 列表的长度
print(len(namelist))

# 根据下标获取列表中的元素
print(namelist[0])

# 获取列表中的元素的后缀名
filenames = ["01.py","02.txt","03.java","04.js"]
# 获取列表中第一个元素中最后一个.出现的下标位置
index = filenames[0].rfind(".")
# 根据字符串切片的方法获取元素的后缀名
print(filenames[0],type(filenames[0]))
print(filenames[0][index:])

# 使用while循环获取列表中每个元素的后缀名
i = 0
while i < len(filenames):
    index = filenames[i].rfind(".")
    print(filenames[i][index:],end=" ")
    i += 1
print("\n")

# 使用高级for循环获取列表中每个元素的后缀名
for temp in filenames:
    # 获取元素中最后一个.出现的下标位置
    index = temp.rfind(".")
    # python默认打印后换行,所以使用end=" "
    print(temp[index:],end=" ")
print("\n")    


















