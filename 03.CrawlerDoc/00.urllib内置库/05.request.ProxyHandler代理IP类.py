# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-26 10:59

# IP代理网站:
# 如: 西刺 https://www.xicidaili.com/nn/
# 如: 快代理 https://www.kuaidaili.com/free/

# ProxyHandler处理器: 代理设置

from urllib import request

url = "http://httpbin.org/get"

# 不使用IP代理
res = request.urlopen(url)
print(res.read().decode('utf-8'))

# 使用IP代理
# 1. 使用ProxyHandler,传入IP代理构建一个handler
# 2. 使用已创建的handler构建以个opener
# 3. 使用opener去发送一个请求open()

handler = request.ProxyHandler({"https":"112.87.71.209:9999"})
opener = request.build_opener(handler)
# req = request.Request(url,headers)  # 如果需要添加请求头信息需要使用Request类
result = opener.open(url)
print(result.read().decode('utf-8'))

