# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 17:33

import copy

### 浅拷贝: 是对于一个对象的顶层拷贝,即拷贝了引用,并没有拷贝内容
### 深拷贝: 是对于一个对象的所有层次的拷贝(递归)

# import copy
    # copy.copy() 浅拷贝
    # copy.deepcopy() 深拷贝

# 浅拷贝对不可变类型与可变类型的copy()不同

a = [1,2,3]
b = [4,5,6]
c = [a,b]
print(c)
# d = copy.copy(c)
d = copy.deepcopy(c)
e = d
print(d)
a.append(7)
print(c)
print(d)

