# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 列表中元素的查找(四种方式)


names = ["zhangsan","lisi","wangwu","liuliu","zhaoqi","chenba"]

### 查找姓名是否在列表中
print("----- ----- -----")
# 思想:0表示没有找到,1表示找到
findflag = 0 
findname = input("你要查找的姓名:")
for name in names:
     
    if findname == name:
        findflag = 1 
        break
    else:
        findflag = 0
 
if findflag == 1:
    print("%s存在与列表中..."%findname)  
else:
    print("你所查找的姓名不存在!!!")
print("----- ----- -----")   


# in:存在,查找元素是否存在,存在返回true,否则返回false
# not in:不存在,查找元素是否不存在,不存在返回true,否则返回false
x = input("你要查找的元素:")
if x in names:
    print("存在...")
else:
    print("不存在!!!")

# index():在列表中的某个下标区间内查找元素是否存在:在列表中找到返回该元素在列表中的下标,否则报错
aaa = [11,15,88,55,66,47,23]
aaa.index(15,1,7 )#注意左闭右开区间

# count():在列表中查找某个元素,查找到返回1,否则返回0
bbb = [11,15,88,55,66,47,23]
bbb.count(88)




