# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### windows系统下：非关系型数据库Redis，客户端软件RedisDesktopManager
import redis

# 链接
red = redis.StrictRedis(host="localhost",port=6379,password="password")

# 方法一：根据数据类型的不同，调用相应的方法
# 写入
# red.set("str","hell")
# 读取
# result = red.get("str")
# print(result)

# 方法二：pipeline
# 缓冲多条命令，然后依次执行，可以减少服务器-客户端的tcp数据包
pipe = red.pipeline()
pipe.set("str2","你好")
pipe.set("str3","你好啊")
pipe.set("str4","nihao")

pipe.execute()
