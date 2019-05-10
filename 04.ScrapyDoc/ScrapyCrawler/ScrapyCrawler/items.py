# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QsbkItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()

class WxappItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    pubdate = scrapy.Field()
    content = scrapy.Field()

class Bmw1Item(scrapy.Item):
    title = scrapy.Field()
    urls = scrapy.Field()

class Bmw2Item(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

class Bmw3Item(scrapy.Item):
    category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()



