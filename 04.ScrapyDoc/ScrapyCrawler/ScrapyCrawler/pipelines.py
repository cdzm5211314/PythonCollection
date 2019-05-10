# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ScrapycrawlerPipeline(object):
    def process_item(self, item, spider):
        # print("*****")
        # print(item)
        # print("*****")
        return item

# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("qsbk.json", "w", encoding="utf-8")
#
#     def open_spider(self,spider):
#         print("爬虫开启了")
#
#     def process_item(self, item, spider):
#         # print(type(item))
#         # item_json = json.dumps(item,ensure_ascii=False)
#         item_json = json.dumps(dict(item),ensure_ascii=False)  # 需要把item格式数据转换成dict字典格式数据
#         self.fp.write(item_json + "\n")
#         print("数据写入完成...")
#         return item
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print("爬虫关闭了")

from scrapy.exporters import JsonItemExporter
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("qsbk.json", "wb")
#         self.exporters = JsonItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
#         self.exporters.start_exporting()
#
#     def open_spider(self,spider):
#         print("爬虫开启了")
#
#     def process_item(self, item, spider):
#         self.exporters.export_item(item)
#         print("数据写入完成...")
#         return item
#
#     def close_spider(self,spider):
#         self.exporters.finish_exporting()
#         self.fp.close()
#         print("爬虫关闭了")

from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("qsbk.json", "wb")
        self.exporters = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")

    def open_spider(self,spider):
        print("爬虫开启了")

    def process_item(self, item, spider):
        # print(type(item))
        self.exporters.export_item(item)
        print("数据写入完成...")
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫关闭了")

from scrapy.exporters import JsonLinesItemExporter
class WxappPipeline(object):
    def __init__(self):
        self.fp = open("wxapp.json", "wb")
        self.exporters = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")

    def process_item(self, item, spider):
        # print(type(item))
        self.exporters.export_item(item)
        print("数据写入完成...")
        return item  # 返回item,是为了给其他pipeline使用

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫关闭了")


import os
from urllib import request
class Bmw1Pipeline(object):
    def __init__(self):
        # 图片存放总目录: 即:E:\workspace_PyCharm\WebCrawler\ScrapyCrawler\ScrapyCrawler\images
        self.path = os.path.join(os.path.dirname(__file__),"images")
        # 判断文件夹是否存在,不存在就创建
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        title = item['title']
        urls = item['urls']
        title_path = os.path.join(self.path,title)
        # 判断图片总目录下是否存在图片类别的目录,不存在就创建
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        # 根据分类目录下载图片
        for url in urls:  # 此处图片是一个一个的下载
            # 把图片下载地址分割,取最后面的作为图片名称
            imagename = url.split('__')[-1]
            # print(imagename)
            # 下载图片并保存到相应的目录下
            request.urlretrieve(url,os.path.join(title_path,imagename))
        return item


# 自定义图片根据分类存储缩略图
from scrapy.pipelines.images import ImagesPipeline
class Bmw2Pipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """这个方法是在发送下载请求之前调用,也是发送下载请求的"""
        request_objs = super(Bmw2Pipeline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        """这个方法是图片将要被存储的时候调用,用来获取这个图片存储的路径"""
        path = super(Bmw2Pipeline,self).file_path(request,response,info)
        title = request.item.get("title")
        from . import settings  # from ScrapyCrawler import settings
        images_store = settings.IMAGES_STORE  # 从setting.py文件获取图片存储位置路径信息
        title_path = os.path.join(images_store,title)  # 拼接图片分类目录
        # 判断图片分类的目录是否存在,不存在就创建
        if not title_path:
            os.mkdir(title_path)
        image_name = path.replace("full/","")
        image_path = os.path.join(title_path,image_name)
        return image_path

# 自定义图片根据分类存储高清图片
from scrapy.pipelines.images import ImagesPipeline
class Bmw3Pipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """这个方法是在发送下载请求之前调用,也是发送下载请求的"""
        request_objs = super(Bmw3Pipeline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        """这个方法是图片将要被存储的时候调用,用来获取这个图片存储的路径"""
        path = super(Bmw3Pipeline,self).file_path(request,response,info)
        category = request.item.get("category")
        from . import settings  # from ScrapyCrawler import settings
        images_store = settings.IMAGES_STORE  # 从setting.py文件获取图片存储位置路径信息
        category_path = os.path.join(images_store,category)  # 拼接图片分类目录
        # 判断图片分类的目录是否存在,不存在就创建
        if not category_path:
            os.mkdir(category_path)
        image_name = path.replace("full/","")
        image_path = os.path.join(category_path,image_name)
        return image_path

