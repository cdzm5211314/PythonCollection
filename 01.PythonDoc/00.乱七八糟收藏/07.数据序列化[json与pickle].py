# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-11-16 14:11

# json： 可以在不同语言之间交换数据,只能序列化最基本的数据类型
# pickle：可以序列化Python中所有的数据类型，包括类，函数都可以序列化

# json 模块提供了四个功能：dumps、dump、loads、load

# pickle 模块提供了四个功能：dumps、dump、loads、load

import json
import pickle

dict1 = {"name":"zhangsan","age":25}

# json序列化数据
json_x = json.dumps(dict1)
print(json_x,type(json_x)) # {"name": "zhangsan", "age": 25} <class 'str'>

# json反序列化数据
json_f = json.loads(json_x)
print(json_f,type(json_f)) # {'name': 'zhangsan', 'age': 25} <class 'dict'>


# pickle序列化数据
pickle_x = pickle.dumps(dict1)
print(pickle_x,type(pickle_x)) # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x08\x00\x00\x00zhangsanq\x02X\x03\x00\x00\x00ageq\x03K\x19u.' <class 'bytes'>

# pickle反序列化数据
pickle_f = pickle.loads(pickle_x)
print(pickle_f,type(pickle_f))  # {'name': 'zhangsan', 'age': 25} <class 'dict'>


