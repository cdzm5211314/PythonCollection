# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

### Python中内置的一种数据类型是列表:list是一种有序的可以重复的集合,可以随便添加与删除
# 列表的元素下标是从0开始
classlist = ["zhangsan","lisi","wangwu","liuliu","xuqi","chenjiu"]
# 查看列表中的元素个数
print(len(classlist))

# 使用下标来访问列表的元素,如果下标超出报错
print(classlist[2])

### 列表的增删改查:

# 列表中元素添加: append() , extend() , insert()
# append()  ---> 在列表的最后位置追加一个元素
classlist.append("chendong")
print(classlist)
# extend()  ---> 将另一个集合中的元素逐一添加到列表中
num1 = ["100","200","300"]
num2 = ["10","20","30"]
num2.extend(num1)
print(num2)
# insert()  ---> 在列表的指定位置前插入一个元素
classlist.insert(0,"Python")
classlist.insert(0,"chendong")
print(classlist)

# 列表中元素查找: in , not in , index() , count()
# in : 如果的查找的元素在列表中,结果返回True,否则返回False
# not in : 如果查找的元素不在列表中,结果返回True,否则返回False
# index()   ---> 查看元素是否在列表中,存在就返回该元素在列表中的下标
print(classlist.index("Python"))
# count()   ---> 查看元素在列表存在的个数
print(classlist.count("chendong"))

# 列表的元素删除: del , pop() , remove()
# del ---> 不属于列表,是Python内置的,可以根据下标删除列表中的元素,也可以删除整个变量的值
del classlist[0]
# del classlist
print(classlist)
# pop() ---> 默认删除列表中最后一个元素,并返回最后一个的元素的值
print(classlist.pop())
# remove()  ---> 根据元素的值进行删除第一个
classlist.remove("Python")
print(classlist)

# 列表中排序: sort() , reverse()
list1 = ["11","22","33","44","55","33"]
# sort()    ---> 默认是按照从小到大的顺序排序,参数 reverse = True 是从大到小排序
list1.sort()
# list1.sort(reverse = True)
print(list1)

# reverse() ---> 把列表中的元素逆置(翻转)
list1.reverse()
# print(list1[-1::-1])
print(list1)

