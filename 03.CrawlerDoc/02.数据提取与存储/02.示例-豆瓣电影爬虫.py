# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-27 11:24

# 1. 将目标网站上的页面爬取下来
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Referer": "https://www.douban.com/"
}
url = "https://movie.douban.com/cinema/nowplaying/beijing/"
response = requests.get(url, headers=headers)
text = response.text
# response.text:         返回是一个解码后的字符串,是str(unicode)类型
# response.content:      返回是一个原生的字符串,从网页上抓取下来的,没有经过处理,是bytes类型

# 2. 将爬取下来的内容按照一定的规则进行数据提取
from lxml import etree
htmlElement = etree.HTML(text)

# 提取豆瓣电影网站北京地区正在上映的的电影名称
titles = htmlElement.xpath('//li[@class="stitle"]/a/@title')   # 正在上映的电影名称列表
imgs = htmlElement.xpath('//li[@class="poster"]/a/img/@src')   # 正在上映的电影的海报图片地址列表
# print(titles)
# print(imgs)

for name, haibao in zip(titles, imgs):
    print("电影名称: " + name, " ---> ", "海报图片: " + haibao)

