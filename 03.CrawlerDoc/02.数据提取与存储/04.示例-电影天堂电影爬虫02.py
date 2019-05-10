# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-27 14:47

# 电影天堂最新上映电影下一页有规律
# url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
# url = "https://www.dytt8.net/html/gndy/dyzz/list_23_2.html"

import requests
from lxml import etree

BASE_URL = "https://www.dytt8.net"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

# 获取电影详情页列表
def get_detail_urls(url_page):
    response = requests.get(url_page, headers=HEADERS)

    htmlElement = etree.HTML(response.content.decode("gbk"))
    detail_list = htmlElement.xpath('//table[@class="tbspan"]//a/@href')  # 电影详情页列表

    # 拼接电影详情页列表
    # detail_urls = map(lambda url: BASE_URL + url, detail_list)
    detail_urls = []
    for url in detail_list:
        # print(BASE_URL + url, len(detail_list))
        detail_urls.append(BASE_URL + url)
    return detail_urls

# 提取电影详情页数据
def detail_parse(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode("gbk")
    htmlElement = etree.HTML(text)
    # title = htmlElement.xpath('//font[@color="#07519a"]')  # 列表
    title = htmlElement.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    img = htmlElement.xpath('//div[@id="Zoom"]//img/@src')[0]
    # print(title,type(title))  # 2018年剧情《库尔斯克/深海救援》BD英语中字 <class 'lxml.etree._ElementUnicodeResult'>
    # print(img,type(img))  # https://www.z4a.net/images/2019/03/20/3.jpg <class 'lxml.etree._ElementUnicodeResult'>
    movie["title"] = title
    movie["img"] = img
    # print(movie)
    return movie

# 爬虫方法
def detail_spider(num):
    # 1. 构建要爬取电影页码数
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for i in range(1, num):  # 1 到 num - 1
        url = base_url.format(i)
        # 2. 获取每页页面的电影详情页列表
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            # print(detail_url)
            # 3. 解析电影详情页,获取数据
            movie = detail_parse(detail_url)
            movies.append(movie)
    return movies

if __name__ == '__main__':
    # 运行爬虫
    movies = detail_spider(2)
    print(movies)



