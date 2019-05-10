# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-11-01 18:17

import time

'''
Python变量与数据类型
    Numbers(数字):    
        int(整型) long(长整型) float(浮点型) complex(复数)
    boolean(布尔):    
        true false
    String(字符串):  
    List(列表): 
    Tuple(元祖):
    Dictionary(字典):

'''
# 查看数据的类型
num = 10
num2 = 7.8
print(type(num))
print(type(num2))

english = 100
math = 85
str = "你好啊"

# 格式化输出
print("我的英语成绩%d,我的数学成绩%d" % (english, math))
print("你在说:%s" % str)

# 换行显示
print("22222222\n33333333")

# 练习:输出一个人的名片
'''
==========
姓名:chendong
QQ:123309778
手机号:18688688688
地址:北京大兴区
==========
'''

name = "chendong"
qq = 123309778
phone = 18688688688
address = "北京大兴区"
print("==========\n姓名:%s\nQQ:%d\n手机号:%d\n地址:%s\n==========" % (name, qq, phone, address))

# 输入
password = input("请输入你的密码:")
print(type(password))
print("你的密码是:%s" % password)

# 升级版的打印名片
name = input("你的姓名:")
qq = input("你的QQ号:")
phone = input("你的手机号:")
address = input("你的地址:")
# 延时三秒打印名片
print("系统正在打印...")
time.sleep(3)
print("==========\n姓名:%s\nQQ:%s\n手机号:%s\n地址:%s\n==========" % (name, qq, phone, address))





