# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 字典的讲解

names = {"name":"zhangsan","address":"luoshan","age":19}
print(names)

# 根据字典的键访问值,当key值不存在时报错
print(names["age"])

# 如果没有key值,则取不到
print(names.get("sex"))

# 根据字典的键修改对应的值
names["address"] = "信阳"
print(names)


# 给字典中添加值
names["id"] = 10
print(names)

# 删除字典中的元素
# del:删除指定的元素
del names["id"]
print(names)

# clear():清空整个字典
names.clear()
print(names)




