# -*- coding: utf-8 -*-
import scrapy
from ScrapyCrawler.items import Bmw2Item


class Bmw2Spider(scrapy.Spider):
    name = 'bmw2'
    allowed_domains = ['autohome.com']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    # 为spider爬虫,配置自己的图片下载pipeline(ImagesPipeline)
    custom_settings = {
        "ITEM_PIPELINES": {
    #         'scrapy.pipelines.images.ImagesPipeline': 1,
            'ScrapyCrawler.pipelines.Bmw2Pipeline': 300,
        }
    }

    def parse(self, response):
        # 获取所有类型图片
        divs_uibox = response.xpath('//div[@class="uibox"]')[1:]
        # print(divs)
        for div in divs_uibox:
            title = div.xpath('.//div[@class="uibox-title"]/a/text()').extract_first()
            urls = div.xpath('.//div[@class="uibox-con carpic-list03"]/ul/li/a/img/@src').extract()
            # 补全urls列表中的url地址: https://
            # response.urljoin(x)与start_urls列表中url地址对比,可以补全url地址
            urls = list(map(lambda x: response.urljoin(x), urls))
            # 推送数据到IMagesPipeline
            print(title,urls)
            yield Bmw2Item(title=title, image_urls=urls)
