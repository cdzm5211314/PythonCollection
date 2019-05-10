# -*- coding: utf-8 -*-
import scrapy
from ScrapyCrawler.items import QsbkItem

class Qsbk2Spider(scrapy.Spider):
    name = 'qsbk2'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    # 为spider设置单独的pipeline(数据不会存到其他的pipeline中)
    custom_settings = {
        "ITEM_PIPELINES": {
            'ScrapyCrawler.pipelines.QsbkPipeline': 300,
        }
    }

    def parse(self, response):
        div_list = response.xpath('//div[@class="col1"]/div')  # 提取所有段子
        item = QsbkItem()
        for div in div_list:
            item["author"] = div.xpath('.//div[@class = "author clearfix"]//img/@alt').extract_first()  # 提取帖子的作者
            item["content"] = div.xpath('.//a//span/text()').extract_first().strip()  # 提取贴子的内容,并去掉内容两端的空格
            yield item  # 推送item数据到pipeline

        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        # print(next_url)
        if not next_url:
            return
        else:
            next_url = "https://www.qiushibaike.com" + next_url
            yield  scrapy.Request(next_url,callback=self.parse)

