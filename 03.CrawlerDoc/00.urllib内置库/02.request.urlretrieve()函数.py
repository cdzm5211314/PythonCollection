# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-25 16:56

from urllib import request

# urlretrieve()函数原型: def urlretrieve(url, filename=None, reporthook=None, data=None):
# urlretrieve()函数作用: 把请求响应的数据保存到本地文件中

result = request.urlretrieve("http://www.baidu.com",'baidu.txt')



