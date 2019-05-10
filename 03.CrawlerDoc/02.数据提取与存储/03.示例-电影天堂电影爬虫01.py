# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-27 14:11

import requests
from lxml import etree

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    # "Referer":"https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
}
BASE_URL = "https://www.dytt8.net"
url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"  # 最新电影的第一页
response = requests.get(url,headers=headers)
# print(response.text)  # 抓取页面内容有乱码
# print(response.content.decode("gbk"))  # 查看网页源代码,发现页面是使用gb2312编码的,所以这里使用gbk解码

htmlElement = etree.HTML(response.content.decode("gbk"))
detail_urls = htmlElement.xpath('//table[@class="tbspan"]//a/@href')  # 电影详情页列表
# print(detail_urls)  # ['/html/gndy/dyzz/20190320/58364.html', '/html/gndy/dyzz/20190320/58363.html']

# 遍历获取电影的详情页列表: https://www.dytt8.net
for detail_url in detail_urls:
    print(BASE_URL+detail_url,len(detail_urls))   # https://www.dytt8.net/html/gndy/dyzz/20190320/58364.html 25



