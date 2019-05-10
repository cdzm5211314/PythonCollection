# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-25 17:04

from urllib import parse

# urlunparse(): 将列表元素拼接成url,接收一个列表的参数，列表的长度必须六个参数以上，要不会抛出异常
url_list = ['http', 'www', 'baidu', 'com', 'dfdf', 'eddffa'] # 这里至少需要6个元素
# print(parse.urlunparse(url_list))


# urljoin(): 将第二个参数的url缺少的部分用第一个参数的url补齐
# 连接两个参数的url, 将第二个参数中缺的部分用第一个参数的补齐,如果第二个有完整的路径，则以第二个为主
# print(parse.urljoin('https://movie.douban.com/', 'index'))
# print(parse.urljoin('https://movie.douban.com/', 'https://accounts.douban.com/login'))


# parse.urlencode()函数的用法: 编码
data = {"name":"张三","age":18}
# print(parse.urlencode(data))  # 编码字典类型的数据: name=%E5%BC%A0%E4%B8%89&age=18

from urllib import request
# url = 'https://www.baidu.com/s?wd=数据库'
# result = request.urlopen(url)  # 报错: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)
url = 'https://www.baidu.com/s'
data = {"wd":"数据库"}
data= parse.urlencode(data)
# print(data)
result = request.urlopen(url + "?" + data)
# print(result.read())


# parse.parse_qs()函数: 解码
data = {"wd":"数据库"}
data= parse.urlencode(data)
print(parse.parse_qs(data))


# parse.urlparse()与parse.urlsplit()函数,对url地址进行分割
url = 'https://www.baidu.com/s?wd=数据库'
# result = parse.urlparse(url)
result = parse.urlsplit(url)
print(result)
print("scheme-协议: ",result.scheme)
print("netloc-域名: ",result.netloc)
print("path-查找路径: ",result.path)
print("query-查询字符串: ",result.query)



