# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 字符串的下标是从0开始
string = " chen521_dong_itcast1314_ chen_itcast_dong.txt   "
# 字符串的长度
print(len(string))

### 字符串的切片:语法 - 字符串[起始:结束:步长]  包含起始下标位置.不包含结束下标位置
# 取字符串下标为0-2的字符(0,1,2)
print(string[0:3])
# 取字符串h到最后的字符
print(string[1:])
# 步长:表示下标位变化的规律 ---> 取字符串从0下标开始到最后,步长为2的字符(即隔个字符取一个)
print(string[0::2])
# 倒序一个字符串
print(string[-1::-1])

### 字符串的常用函数操作:
# find()    ---> 结果是查找到的这个字符串的第一个字符的下标位置,没查找到返回-1
print(string.find("itcast"))
print(string.rfind("itcast"))  # 从右边开始查找
# index()   ---> 结果是查找到的这个字符串的第一个字符的下标位置,没查找到报错
print(string.index("dong"))
print(string.rindex("dong"))  # 从右边开始查找

# count()    ---> 返回一个字符串在另一个字符串中出现的次数
print(string.count("do"))
# replace()  ---> 把一个字符串中的某个字符替换成另一个字符,替换不超过count次
print(string.replace("_","*"))
print(string.replace("_","*",2))  # 表示_号替换*号,只替换两处,

# split()   --->分割:以一个字符为分割符切片某个字符串,返回的是一个列表
print(string.split("_"))
print(string.split("_",2))  #后面有值的话表示仅分割两次

# capitalize()  ---> 把字符串的第一个字符大写
print(string.capitalize())
# title()   ---> 把字符串的每个单词首字母大写
print(string.title())
# lower()   ---> 转换字符串的所有大写字符为小写
print(string.lower())
# upper()   ---> 转换字符串的所有小写字符为大写
print(string.upper())

# startswith()  ---> 检查字符串是否是已某个字符串开头,是返回True,不是返回False
print(string.startswith("dong"))
# endswith()    ---> 检查字符串是否是已某个字符串结尾,是返回True,不是返回False
print(string.endswith(".txt"))

# ljust()   ---> 返回一个原字符串左对齐,并使用空格填充至长度 多少位的新字符串
print(string.ljust(50))
# rjust()   ---> 返回一个原字符串右对齐,并使用空格填充至长度 多少位的新字符串
print(string.rjust(50))
# center()  ---> 返回一个原字符居中对齐,并使用空格填充至长度 多少位的新字符串
print(string.center(50))

# lstrip()  ---> 删除字符串左边的空白字符
print(string.lstrip())
# rstrip()  ---> 删除字符串右边的空白字符
print(string.rstrip())
# strip()   ---> 删除字符串两端的空白字符
print(string.strip())

# splitlines()  ---> 根据换行符分割,返回一个包含各行元素的列表
lines = "adk\nah\nkahdo\nioqwue"
print(lines.splitlines())

# isalpha() ---> 如果字符串所有的字符都是字母,返回True,否则返回false
print(lines.isalpha())
# isdigit() ---> 如果字符串只包含数字,返回True,否则返回false
print(lines.isdigit())
# isalnum() ---> 如果字符串所有字符都是字母或都是数字,返回True,否则返回false
print(lines.isalnum())
# isspace() ---> 如果字符串中只包含空格,返回True,否则返回False
print(lines.isspace())

# join()    ---> 使用字符串把列表中的元素链接起来组成一个新的字符串
list = ["100","200","300"]
str = "chen"
print(str.join(list))
print("".join(list))


### 给定一个字符串,返回使用空格或者\t分割后的倒数第二个子串
# 注: split()  ---> 默认会自动以空格或者"\t"或者其他特殊符号分割字符串
string = " kjls\njd dsda sd\tsd \nwrw er"
print(string.split())
print(string.split()[-2])