# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-26 14:01

# cookie数据的格式: Set－Cookie: NAME=VALUE；Expires=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE
# 如: Set-Cookie:H_PS_PSSID=1424_21097_28723_28558_28697_28585_22158; path=/; domain=.baidu.com

# cookie参数详解:
# 1. NAME: cookie的名字
# 2. VALUE: cookie的值
# 3. Expires: cookie的过期时间
# 4. Path: cookie作用的路径
# 5. Domain: cookie作用的域名
# 6. SECURE: 是否只在https协议下起作用

from urllib import request

login_before = "http://www.renren.com/SysHome.do"  # 人人网登陆页面
login_after = "http://www.renren.com/893394172/profile"  # 人人网登陆后个人主页

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Cookie":"anonymid=jtpd8l73-kbnu9w; depovince=GW; _r01_=1; JSESSIONID=abcKxe6-uz3U-fd0nK4Mw; ick_login=17af5e13-8091-4915-b704-ba0dd553a56c; ick=2cebb1a8-320f-409f-b97c-d7689da8ea12; first_login_flag=1; ln_uact=18103763930; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=09416abf-1d11-4c6c-8467-da91b972e2bc%7C5b34e73601acb25887c4068b9cf69955%7C1553579872178%7C1%7C1553579871820; jebecookies=b17c717a-60d0-41e2-b6e1-8d14325adb62|||||; _de=3F1C6150E59B993580B4C5FE015D8D28; p=a31aab50cb8d58a4f779dfd1cf9c348c2; t=1da5424772e1107fe8c4e9fc60151a562; societyguester=1da5424772e1107fe8c4e9fc60151a562; id=893394172; xnsid=475dd7b9; loginfrom=syshome; wp_fold=0"
}

req = request.Request(url=login_after, headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode("utf-8"))
# with open("cookie.html",'wb') as ft:
#     ft.write(resp.read())
