# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-01-07 21:49

import requests

# url地址的编解码
r1 = requests.utils.quote('https://tieba.baidu.com/?kw=李毅')
r2 = requests.utils.unquote('https://tieba.baidu.com/?kw=%E6%9D%8E%E6%AF%85')
print(r1)  # https%3A//tieba.baidu.com/%3Fkw%3D%E6%9D%8E%E6%AF%85
print(r2)  # https://tieba.baidu.com/?kw=李毅

# 处理不信任的SSL证书: verify = False
r3 = requests.get('https://www.12306.cn/mormhweb/',verify = False)
print(r3)

# 设置超时参数: timeout = 1
r4 = requests.get('http://www.baidu.com',timeout = 1)
print(r4)

# 配合状态码判断是否请求成功
# assert response.status_code == 200

# response = requests.get(url)
# data_dict = response.json()
# 当请求获取到的是json数据时,,使用response.json()会把json数据自动load成字典类型数据
# 如果不是json数据,使用response.json()会报错



