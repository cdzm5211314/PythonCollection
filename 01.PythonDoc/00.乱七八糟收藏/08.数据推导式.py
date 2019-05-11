# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 16:10

### range(1,10) 获取一个包头不包尾的范围对象

### 生成一个1-9的数字列表
list1 = [i for i in range(1,10)]
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

### 生成一个1-9的数字平方的列表
list2 = [ i**2 for i in range(1,10)]
print(list2) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

list3 = [x for x in range(1,3) for y in range(0,2)]
print(list3) # [1, 1, 2, 2]

list4 = [(x,y) for x in range(1,3) for y in range(0,2)]
print(list4) # [(1, 0), (1, 1), (2, 0), (2, 1)]

### 使用推导式取出1-100之间的所有奇数
list5 = [x for x in range(1,101) if x % 2 == 1]
print(list5)

### 使用推导式生成一个[[1,2,3],[4,5,6]...]的列表最大值在100以内
list6 = [ [1+i,2+i,3+i] for i in range(0,98) if i % 3 == 0]
print(list6)

### 字典推导式
cookie =  "anonymid=jv6dyp5urxfloa; depovince=TJ; _r01_=1; JSESSIONID=abcEiDBh_LLekhZF2P3Pw; ick_login=c81f36f8-e2f0-4cf8-accd-3ddb2c5737f9; first_login_flag=1; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=f6c56656-a49d-4595-8574-38c165c15614%7C5b34e73601acb25887c4068b9cf69955%7C1556785777949%7C1%7C1556785780059; wp_fold=0; ln_uact=123309778@qq.com; jebecookies=3627846e-80f2-4b1a-8df4-2ef983db3717|||||; _de=CBAB31EED2C8716972FFEFECAA50653A696BF75400CE19CC; p=87a5e6b37fa38cdef7b27d11c5b684f32; t=93fab4e742e141192b9422897df4fe232; societyguester=93fab4e742e141192b9422897df4fe232; id=893394172; xnsid=884f4b2d; ver=7.0; loginfrom=null"

print({i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ") })




