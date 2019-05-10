# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-26 8:52

# 如果想在请求的时候添加一些请求头信息,那么就必须使用request.Request类
# 如: 添加User-Agent , data ...

from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
}
url = "http://www.baidu.com"

# Request类的初始化方法:__init__
# def __init__(self, url, data=None, headers={},
#                  origin_req_host=None, unverifiable=False,
#                  method=None):

req = request.Request(url=url, headers=headers)  # urllib.request.Request 类的对象
result = request.urlopen(req)  # http.client.HTTPResponse
# print(result.read())  # 字节数据
print(result.read().decode("utf-8"))  # 字符串数据
