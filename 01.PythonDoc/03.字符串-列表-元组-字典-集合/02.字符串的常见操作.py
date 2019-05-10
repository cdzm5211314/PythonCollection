# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23
# 字符串的常见操作

str = "hello word itcast and itcastpython"

# 字符串的长度
print(len(str))

# find():在字符串中查找指定的字符串,当查找到了返回该字符串第一次出现的下标,否则返回-1
print(str.find("it"))
print(str.find("chen"))

# 在字符串从某个下标开始查找,查找到哪个下标为止,查找到返回该字符串的下标,否则返回-1
print(str.find("and",16,45))

# index():都是在字符串中查找某个字符串,查找到返回该下标,index()查找不到报异常

# find():默认从左边找
# rfind():默认从右边找
# index():默认从左边找
# rindex():默认从右边找

# 练习:查看文件名字的后缀
temp = "java.python.py"

# 步骤一:先查找从文件名称右边开始出现的第一个点.的角标
index = temp.rfind(".")
# 步骤二:使用字符串切片
print(temp[index:])

# count():返回一个字符串在start和end位置之间在另一个字符串中出现的次数
mystr1 = "aabbhdaaghjaa"
print(mystr1.count("aa",0,15))

# replace():把mystr2中的str1替换成str2,如果后边有第三个参数,表示替换几个
mystr2 = "sddd**sdds**kkf**ee*wqe"
mystr22 = mystr2.replace("**", "  ",1)
print(mystr22)

# split():已str3分割字符串mystr3,后边有参数的话,表示分割几次
mystr3 = "hello word chen dong"
mystr33 = mystr3.split(" ",2)
print(mystr33)

# capitalize():把字符串的首字母大写
mystr4 = "chendong"
mystr44 = mystr4.capitalize()
print(mystr44)

# title():把字符串的每个首字母大写
mystr5 = "chen dong"
mystr55 = mystr5.title()
print(mystr55)

# startswith():检查字符串是否以xx开头,是返回true,否则返回false
# endswith():检查字符串是否以xx结尾,是返回true,否则返回false
mystr6 = "xxchen"
print(mystr6.startswith("xx"))
print(mystr6.endswith("x"))

# lower():转换字符串中的所有大写为小写
# upper():转换字符串中的所有小写为大写
mystr7 = "HHssFFgggRx"
print(mystr7.lower())
print(mystr7.upper())


# ljust():返回一个原字符串左对齐,使用空格填充至长度width的新字符串
# rjust():返回一个原字符串右对齐,使用空格填充至长度width的新字符串
# center():返回一个原字符串居中,使用空格填充至长度width的新字符串
mystr8 = "itcast"
print(mystr8.ljust(13))
print(mystr8.rjust(13))
print(mystr8.center(13))

# lstrip():删除字符串左边的空格
# rstrip():删除字符串右边的空格
# strip():删除字符串两边的空格
mystr9 = "    你好啊 说你         "
print(mystr9.lstrip())
print(mystr9.rstrip())
print(mystr9.strip())

# isspace():判断字符串是否是空格,是返回true,否则返回false
mystr10 = "adadaawe"
print(mystr10.isspace())





