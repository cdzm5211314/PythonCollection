# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 字典的常见操作


dict = {"name":"chendong","age":18,"sex":"男","id":10}

# len():字典的长度
print(len(dict))

# keys():返回字典中所有key键的列表
print(dict.keys())

# valuses():返回字典中所有value值的列表
print(dict.values())

# items():把字典中的键值对信息取出来放入元组中,并保存在列表中
temp = dict.items()
print(temp)
for key,value in temp:
    print(key,value)

# has_key():如果key在字典中,返回true,否则返回false    ---> python2中有这个方法
# dict.has_key("name")

#字典的遍历key-value(键值对)
for key,value in dict.items():
    print("key=%s, value=%s"%(key,value))


#enumerate():
names = ["张三","李四","王五"]
for i,name in enumerate(names):
    print(i,name)

