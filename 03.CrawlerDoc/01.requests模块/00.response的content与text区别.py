# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-01-06 17:35

# str 使用encode方法转换为 bytes
# bytes 使用decode转换为 str
# 注: 编码方式与解码方式必须一致

str = "陈"
print(type(str))

bb = str.encode()  # 默认为utf-8的方式编码
bb1 = str.encode("gbk")  # 指定gdk的方式编码
print(bb,type(bb))
print(bb1,type(bb1))

ss = bb.decode()  # 默认为utf-8的方式解码
ss1 = bb1.decode("gbk")  # 指定gdk的方式解码
print(ss,type(ss))
print(ss1,type(ss1))


# response.content与response.text的区别:
# 1. response.content: 是从网络上直接抓取的数据,未经过任何解码,所以是一个bytes类型数据,
#                      其实在网络与硬盘上传输的字符串数据都是bytes类型
# 2. response.text: 这个是str数据类型,requests库将response.content进行解码的字符串,解码需要制定一个编码方式,
#                   requests会根据自己来判断编码的方式,所以有时候回猜错,导致解码失败,产生乱码,
#                   所以使用requests.content.decode("utf-8")进行手动解码


