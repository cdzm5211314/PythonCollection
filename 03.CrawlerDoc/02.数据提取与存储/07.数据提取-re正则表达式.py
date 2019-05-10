# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-27 9:31

### 正则表达式语法:
# .	        匹配任意单个字符
# \d	    匹配任意数字，等价于0‐9
# \D	    匹配任意非数字
# \w	    单词字符，等价于A‐Z,a‐z,0‐9,_
# \W        与\w相反
# \s        匹配空白字符(\n,\t,\r,空格)
# *	        前一个字符0次或无限次扩展	            abc* 表示ab、abc、abcc、abccc等
# +	        前一个字符1次或无限次扩展	            abc+ 表示abc、abcc、abccc等
# ?	        前一个字符0次或1次扩展	                abc? 表示ab、abc
# ^	        匹配字符串开头	                        ^abc表示abc且在一个字符串的开头
# $	        匹配字符串结尾	                        abc$表示abc且在一个字符串的结尾
# [  ]	    字符集，对单个字符给出取值范围     	    [ab]表示a、b，[a-z]表示a到z单个字符
# [^  ]	    非字符集，对单个字符给出排除范围	    [^abc]表示非a或b或c的单个字符
# ( )	    分组标记，内部只能使用| 操作符	        (abc)表示abc，(abc|def)表示abc、def

import re

text = "hellowordchenzhangsanlisiaaabbbcccaaaxxx"

# 匹配某个字符
result = re.match("he",text)  # 从字符串的第一个字符开始查找,如果第一个字符满足才往下查找,如果不满足group提取报错
# print(result.group())  # group提取匹配的字符串

# 点. 匹配任意的字符,注: .不能匹配到换行符
result = re.match(".",text)  # 匹配任意单个字符
# print(result.group())

# \d 匹配任意的数字[0-9]
result = re.match("\d","22234")
# print(result.group())

# \D 匹配任意的非数字
result = re.match("\D","@#23$4%")
# print(result.group())

# \s 匹配空白字符(\n,\t,\r,空格)
result = re.match("\s"," asd ")
# print(result.group())

# \w 匹配的是a-z,A-Z,0-9,_
result = re.match("\w","_wasd ")
# print(result.group())

# \W 匹配与\w相反
result = re.match("\W","@_wasd ")
# print(result.group())

# [] 组合的方式
result = re.match("[\d\-]+","0376-8888888abc")
# print(result.group())

# 匹配多个字符
result = re.match("\d+","0376")
# print(result.group())
result = re.match("\w+","abcaabbcc")
# print(result.group())
result = re.match("\w{1,4}","abcaabbcc")
# print(result.group())

#####小示例#####
# 验证手机号: 以1开头,第二位3,5,6,7,8后面9位就随意数字
result = re.match("1[35678]\d+","18103763930")
# print(result.group())
result = re.match("1[35678]\d{9}","18103763930")
# print(result.group())

# 验证邮箱: 邮箱名称是由a-z,A-Z,0-9,_组成的,然后是@符号,后面是域名
result = re.match("\w+@[a-z0-9]+\.[a-z]+","configrueadmin@163.com")
# print(result.group())

# 验证URL: 规则是前面https或http或ftp,后面是冒号+双斜杠,再后面就是任意非空白字符
result = re.match("(https|http|ftp)://[^\s]+","https://www.baidu.com")
# print(result.group())

# 验证身份证: 身份证是18位,前17位是数字,最后一个可能是数字也可能是字符
result = re.match("\d{17}[a-zA-Z0-9]","41152119890312123x")
# print(result.group())

# 转义字符
result = re.search("\$(\d+)","ass dsf $456")
# print(result.group())
result = re.search("\$\d+","ass dsf $456")
# print(result.group())
result = re.search("\\n\w+","dsf $456\nabc")
# print(result.group())
result = re.search("\\\\n\w+",r"dsf $456\nabc")  # r"dsf $456\nabc"  原生字符串
# print(result.group())
result = re.search(r"\\n\w+",r"dsf $456\nabc")  # r"dsf $456\nabc"  原生字符串
# print(result.group())

### re模块的基本使用(功能函数)
# re.match()      从一个字符串的开始位置起匹配正则表达式，返回match对象(从头找一个)
# re.search()     在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象(找一个)
# re.findall()    搜索字符串，以列表类型返回全部能匹配的子串(找所有)
# re.sub()        在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串(替换)
# re.split()      将一个字符串按照正则表达式匹配结果进行分割，返回列表类型(分割)
# re.finditer()   搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
# re.compile()

# 示例: findall(), sub()
result = re.findall("\$\d+","abc $99def  $123xyz")  # 获取价格信息
# print(result)  # ['$99', '$123']
result = re.findall('a(.*?)b','aa456bb')  # 能够返回括号中的内容,括号前后的内容起到定位于过滤的作用
# print(result)  # 'a456'
result = re.sub("\$","#","abc $99def  $123xyz")  # 把字符串中$替换成#
# print(result)  # abc #99def  #123xyz

# 示例: split()
result = re.split("-","abc-def-ghj")
print(result)  # ['abc', 'def', 'ghj']
result = re.split("-","abc-def-ghj-")
print(result)  # ['abc', 'def', 'ghj', '']


