# -*- coding:utf-8 -*-
# @Desc :
# @Author : Administrator
# @Date : 2019-03-28 20:51

import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

# 生产者
class Producer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    def __init__(self,page_queue,img_url_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_url_queue = img_url_queue
    def run(self):
        while True:
            if self.page_queue.empty():  # 判断队列是否为空,为空就停掉
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        # requests请求网站
        response = requests.get(url, headers=self.headers)
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
            self.img_url_queue.put((img_url,img_file_name))

# 消费者
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_url_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_url_queue = img_url_queue

    def run(self):
        while True:
            if self.img_url_queue.empty() and self.page_queue.empty():  # 判断两个队列是否为空,为空就停掉
                break
            img_url,img_file_name = self.img_url_queue.get()
            request.urlretrieve(img_url, 'imges/' + img_file_name)  # 下载表情图片
            print(img_file_name + "下载完成...")

def main():
    page_queue = Queue(100)  # 存储页码的队列
    img_url_queue = Queue(1000)  # 存储图片url地址的队列

    # doutula = "https://www.doutula.com/photo/list/?page=3"
    base_url = "https://www.doutula.com/photo/list/?page={}"
    for i in range(1, 11):  # 获取斗图啦[doutula.com]前5页的图片
        url = base_url.format(i)
        page_queue.put(url)
        # break  # 测试时执行一次

    for i in range(5):  # 创建5个生产者线程
        t = Producer(page_queue,img_url_queue)
        t.start()
    for i in range(5):  # 创建5个消费者线程
        t = Consumer(page_queue,img_url_queue)
        t.start()

if __name__ == '__main__':
    main()



