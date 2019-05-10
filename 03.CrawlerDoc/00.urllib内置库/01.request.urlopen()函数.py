# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-25 16:25

from urllib import request

# 在Python3的urllib库中,所有和网络相关的方法都被集中到urllib.request模块下面
# urllib函数解析:
# 1. url: 请求的url
# 2. data: 请求的data,如果设置了这个值,那么就变成post请求
# 3. 返回值: 返回值是一个http.client.HTTPResponse对象,这个对象是一个类文件句柄对象,有如下方法
# 3.1 read():  读取响应的所有数据,字节bytes数据
# 3.2 readline(): 读取响应的一行数据,字节bytes数据
# 3.3 readlines(): 读取响应的多行数据,字节数据bytes列表
# 3.4 getcode(): 获取请求后的响应状态码
# 3.5 geturl(): 返回URL的资源检索,常常重定向之后使用

# def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#             *, cafile=None, capath=None, cadefault=False, context=None):

result = request.urlopen('http://www.baidu.com')

# print(result)
# print(result.read())
print(result.read().decode('utf-8'))  # 把获取到的响应数据进行编码
# print(result.readline())
# print(result.readlines())
print(result.getcode())
print(result.geturl())



