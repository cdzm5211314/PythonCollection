# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ScrapyCrawler.items import Bmw3Item


class Bmw3Spider(CrawlSpider):
    name = 'bmw3'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    # 为spider爬虫,配置自己的高清图片下载pipeline(ImagesPipeline)
    custom_settings = {
        "ITEM_PIPELINES": {
            'ScrapyCrawler.pipelines.Bmw3Pipeline': 200,
        }
    }

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65-.+'), callback='parse_page', follow=False),
    )

    def parse_page(self, response):
        # 图片的类别
        category = response.xpath('//div[@class="uibox"]/div[@class="uibox-title"]/text()').extract_first()
        # 分类图片地址列表(缩略图)
        src_urls = response.xpath(
            '//div[@class="uibox"]/div[@class="uibox-con carpic-list03 border-b-solid"]//img/@src').extract()
        # print(category,src_urls)
        # 把缩略图地址更换为高清图片地址
        src_urls = list(map(lambda x: x.replace("t_", ""), src_urls))
        # 第一种方式: 给高清图片地址加上前缀: https://
        # image_urls = []
        # for src in src_urls:
        #     url = response.urljoin(src)
        #     image_urls.append(url)
        # 第二种方式: 给高清图片地址加上前缀: https://
        image_urls = list(map(lambda x: response.urljoin(x), src_urls))
        print(category, image_urls)
        # 推送数据到pipeline
        yield Bmw3Item(category=category, image_urls=image_urls)

