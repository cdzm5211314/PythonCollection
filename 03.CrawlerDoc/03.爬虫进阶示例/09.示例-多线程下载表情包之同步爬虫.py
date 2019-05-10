# -*- coding:utf-8 -*-
# @Desc :
# @Author : Administrator
# @Date : 2019-03-28 19:55

import requests
from lxml import etree
from urllib import request
import os
import re

def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    # requests请求网站
    response = requests.get(url, headers=headers)
    text = response.content.decode("utf-8")  # response.text也可以使用,只要没有乱码
    # 使用etree创建Element对象
    htmlElement = etree.HTML(text)
    # 因为存在动态gif图,所以需要过滤掉
    imgs = htmlElement.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    for img in imgs:
        # print(etree.tostring(img))
        # img_url = img.xpath('./@data-original')[0]  # 获取图片的url地址
        img_url = img.get("data-original")  # 获取图片的url地址
        img_title = img.get("alt")  # 获取图片的名字
        img_title = re.sub(r'[\?？\.，。！!]','',img_title)  # 根据正则去掉图片的名字的特殊字符
        img_suffix = os.path.splitext(img_url)[1]  # 分割图片后缀名, .jpg和.jpg!dta
        img_suffix = img_suffix.split("!")[0]  # 再根据字符串分割后缀名
        # print(img_suffix)
        img_file_name = img_title + img_suffix  # 组成下载的图片名及后缀名
        # print(img_url,img_title,img_suffix)
        request.urlretrieve(img_url,'imges/'+img_file_name)  # 下载表情图片
        print(img_file_name + "下载完成!!!")

def main():
    # doutula = "https://www.doutula.com/photo/list/?page=3"
    base_url = "https://www.doutula.com/photo/list/?page={}"
    for i in range(1, 6):  # 获取斗图啦[doutula.com]前5页的图片
        url = base_url.format(i)
        parse_page(url)
        break  # 测试时执行一次

if __name__ == '__main__':
    main()