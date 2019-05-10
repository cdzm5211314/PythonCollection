# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-01-02 21:12

# str 使用encode方法转换为 bytes
# bytes 使用decode转换为 str
# 注: 编码方式与解码方式必须一致

str = "陈"
print(type(str))

bb = str.encode()  # 默认为utf-8的方式编码
bb1 = str.encode("gbk")  # 指定gdk的方式编码
print(bb,type(bb))
print(bb1,type(bb1))

ss = bb.decode()  # 默认为utf-8的方式解码
ss1 = bb1.decode("gbk")  # 指定gdk的方式解码
print(ss,type(ss))
print(ss1,type(ss1))




