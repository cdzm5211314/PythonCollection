# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

### Python中内置了字典,使用键值(key-value)对存储数据,查找速度快,键(key)不能重复

info = {"name":"zhangsan","age":18,"sex":"f"}
### 访问字典中某个键的值
# dict["key"]   ---> 当在字典中查找这个键时,返回对应的键的值,否则报错
print(info["name"])
# print(info["addr"])
# dict.get("key")   ---> 当在字典中查找这个键时,返回对应的键的值,否则没有结果(None)
print(info.get("age"))
print(info.get("addr"))

### 字典(dict)的常用操作:
# len(dict)   ---> 字典的键值对个数

# dict["key"] = "value"   # 当这个key不存在字典中就是一个新增操作

# dict.keys()   ---> 返回一个包含所有key的列表
for key in info.keys():
    print(key,end = " ")
# dict.values()   ---> 返回一个包含所有value的列表
for value in info.values():
    print(value,end = " ")
# dict.items()  ---> 返回一个包含所有(键,值)元组的列表
for item in info.items():
    print(item,end = " ")

# del dict["key"]   ---> 删除字典中的元素
# del dict  ---> 删除整个字典
# dict.clere()   ---> 清空整个字典
