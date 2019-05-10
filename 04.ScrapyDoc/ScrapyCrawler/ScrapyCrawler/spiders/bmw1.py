# -*- coding: utf-8 -*-
import scrapy
from ScrapyCrawler.items import Bmw1Item

class Bmw1Spider(scrapy.Spider):
    name = 'bmw1'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    # 为spider设置单独的pipeline(数据不会存到其他的pipeline中)
    custom_settings = {
        "ITEM_PIPELINES": {
            'ScrapyCrawler.pipelines.Bmw1Pipeline': 300,
        }
    }

    def parse(self, response):
        # 获取所有类型图片
        divs_uibox = response.xpath('//div[@class="uibox"]')[1:]
        # print(divs)
        for div in divs_uibox:
            title = div.xpath('.//div[@class="uibox-title"]/a/text()').extract_first()
            # print(title)
            urls = div.xpath('.//div[@class="uibox-con carpic-list03"]/ul/li/a/img/@src').extract()
            # print(urls)
            # 补全urls列表中的url地址: https://
            # response.urljoin(x)与start_urls列表中url地址对比,可以补全url地址
            urls = list(map(lambda x: response.urljoin(x), urls))
            # 推送数据到pipeline
            yield Bmw1Item(title=title,urls=urls)