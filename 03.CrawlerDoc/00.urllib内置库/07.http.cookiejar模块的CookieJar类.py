# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-26 14:23

# http.cookiejar模块主要的类有: CookieJar, FileCookieJar, MozillaCoookieJar, LWPCookieJar
# CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
#            整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

# login_before = "http://www.renren.com/PLogin.do"  # 人人网登陆页面
# login_after = "http://www.renren.com/893394172/profile"  # 人人网登陆后个人主页

from urllib import request, parse
from http.cookiejar import CookieJar

# 1. 登陆
# 1.1 创建CookieJar对象
cookiejar = CookieJar()
# 1.2 使用CookieJar对象创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 使用上一步的handler创建一个opener
opener = request.build_opener(handler)
# 1.4 使用opener发送登陆请求(人人网的账号和密码)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
data = {
    "email": "1810376****",
    "password": "****123456"
}
login_before = "http://www.renren.com/PLogin.do"  # 人人网登陆页面
req = request.Request(url=login_before, data=parse.urlencode(data).encode("utf-8"), headers=headers)
resp = opener.open(req)

# 2. 访问个人主页
# 获取个人主页页面的时候,不需要新建opener,而是使用之前创建的opener,之前的opener包含了登陆所需要的cookie信息
login_after = "http://www.renren.com/893394172/profile"  # 人人网登陆后个人主页
req2 = request.Request(url=login_after, headers=headers)
resp2 = opener.open(req2)
with open("renren.html", 'wb') as ft:
    ft.write(resp.read())
