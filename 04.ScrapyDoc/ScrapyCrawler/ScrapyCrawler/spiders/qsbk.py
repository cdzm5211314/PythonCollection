# -*- coding: utf-8 -*-
import scrapy
from ScrapyCrawler.items import QsbkItem

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    # 为spider设置单独的pipeline(数据不会存到其他的pipeline中)
    custom_settings = {
        "ITEM_PIPELINES": {
            'ScrapyCrawler.pipelines.QsbkPipeline': 300,
        }
    }

    def parse(self, response):
        # print(type(response))  # <class 'scrapy.http.response.html.HtmlResponse'>
        # response.text  # 是解码后的内容
        # response.bady  # 是未解码的内容
        div_list = response.xpath('//div[@class="col1"]/div')  # 提取所有段子
        # print(div_list)
        # for div in div_list:
        #     author = div.xpath('.//div[@class = "author clearfix"]/a[1]/img/@alt').extract_first()
        #     content = div.xpath('.//a//span/text()').extract_first().strip()
        #     # print(author,content)
        #     # yield 只能推送字典类型数据和item类型数据到pipeline.
        #     duanzi = {"author":author,"content":content}
        #     yield duanzi
        # 推送item类型数据到pipeline中.
        item = QsbkItem()
        for div in div_list:
            item["author"] = div.xpath('.//div[@class = "author clearfix"]/a[1]/img/@alt').extract_first()
            item["content"] = div.xpath('.//a//span/text()').extract_first().strip()
            yield item
        # for div in div_list:
        #     author = div.xpath('.//div[@class = "author clearfix"]/a[1]/img/@alt').extract_first()
        #     content = div.xpath('.//a//span/text()').extract_first().strip()
        #     yield QsbkItem(author = author,content=content )



