# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 列表中删除元素(del,pop,remove)


filenames1 = ["01.py","02.txt","03.c","04.php","05.doc","07.java"]

# del():根据下标删除元素
print(filenames1)
del filenames1[2]
print(filenames1)

print("===== ===== =====")

# pop():删除列表中最后一个元素
filenames2 = ["01.py","02.txt","03.c","04.php","05.doc","07.java"]
print(filenames2)
filenames2.pop()
print(filenames2)

print("===== ===== =====")

# remove():根据元素的值进行删除
filenames3 = ["01.py","02.txt","03.c","04.php","05.doc","07.java"]
print(filenames3)
filenames3.remove("05.doc")
print(filenames3)

print("===== ===== =====")




