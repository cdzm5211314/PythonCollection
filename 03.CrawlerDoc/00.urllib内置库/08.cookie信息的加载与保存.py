# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-26 15:43

# http.cookiejar模块主要的类有: CookieJar, FileCookieJar, MozillaCoookieJar, LWPCookieJar
# MozillaCookieJar (filename,delayload=None,policy=None)：
# 从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

from http.cookiejar import  MozillaCookieJar
from urllib import request

mozillacookiejar = MozillaCookieJar("cookie.txt")
handler = request.HTTPCookieProcessor(mozillacookiejar)
opener = request.build_opener(handler)

# 把cookie信息保存在本地文件中
# resp = opener.open("http://www.baidu.com")
opener.open("http://httpbin.org/cookies/set?user=zhangsan")
mozillacookiejar.save(ignore_discard=True)

# 把文件中的cookie信息读取出来
mozillacookiejar.load(ignore_discard=True)
opener.open("http://httpbin.org/cookies")
for cookie in mozillacookiejar:
    print(cookie)
