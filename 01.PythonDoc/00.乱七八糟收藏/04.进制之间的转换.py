# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 18:37

### 把一个十进制的数字转换为二进制,八进制,十六进制
num = 12
# 转换为二进制 : bin()
print(bin(num))
# 转换为八进制 : oct()
print(oct(num))
# 转换为十六进制 : hex()
print(hex(num))

### 把二进制,八进制,十六进制转换为十进制
# 如: 二进制:"0b1100" 八进制:"0o14" 十六进制:"0xc"
print(int("0b1100",2))
print(int("0o14",8))
print(int("0xc",16))
