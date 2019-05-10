# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-9-13 14:06

### 模块的分类:
#   标准库: Python解释器内置的模块
#   开源模块:
#   自定义模块:

## 时间模块: time 与 datetime
#   时间的表示方式:1.时间戳 2.格式化的时间字符串 3.元组(struct_time):共九个元素

import time
# 获取时间戳
# print(time.time())

# 睡几秒
# time.sleep(3)
# print("我睡了多久")

# 获取时间元组struct_time[tuple](参数为时间戳)
# print(time.localtime())  # 获取本地时区的当前时间元组
# print(time.gmtime())  # 获取当前时间的标准时间元组格式

### 将时间戳 转换成 时间元组的形式
# tup = time.localtime(1316546464)
# print(tup)
# print(tup.tm_year)

### 将时间元组 转换成 时间戳形式
# t = time.localtime()  # 当前时间元组
# print(time.mktime(t))

### 将时间元组 转换成 时间格式的字符串
# t = time.localtime()
# tstr = time.strftime("%Y-%m-%d %H:%M:%S",t)
# print(tstr)


### 将时间格式化字符串 转换成 时间元组
# tt = time.strptime("2017-05-25 14:32:58","%Y-%m-%d %H:%M:%S")
# print(tt)



### 将时间元组 转换成 默认的时间格式的字符串: 参数--->时间元组,无参数默认为当前时间元组
# print(time.asctime())
### 将时间戳 转换成 默认的时间格式的字符串: 参数--->时间戳,无参数默认为当前的时间戳
# print(time.ctime())



import datetime
### datetime模块中有三个类
#   tate : 表示年月日
#   time : 表示时分秒
#   datetime : 表示年月日时分秒

print(datetime.datetime.now())  # 获取当前时间
print(datetime.datetime.now() + datetime.timedelta(3))  # 获取当前时间三天后的时间
print(datetime.datetime.now() + datetime.timedelta(-3))  # 获取当前时间三天前的时间
print(datetime.datetime.now() + datetime.timedelta(hours = 5))  # 获取当前时间五小时后的时间
print(datetime.datetime.now() + datetime.timedelta(hours = -5))  # 获取当前时间五小时前的时间
print(datetime.datetime.now() + datetime.timedelta(minutes = 20))  # 获取当前时间二十分钟后的时间
print(datetime.datetime.now() + datetime.timedelta(minutes = -20))  # 获取当前时间二十分钟前的时间

print(datetime.datetime.now().replace(minute=30,hour = 2))  # 替换当前时间






