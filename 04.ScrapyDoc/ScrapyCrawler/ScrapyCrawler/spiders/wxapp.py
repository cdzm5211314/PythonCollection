# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ScrapyCrawler.items import WxappItem

class WxappSpider(CrawlSpider):
    name = 'wxapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    # 为spider设置单独的pipeline(数据不会存到其他的pipeline中)
    custom_settings = {
        "ITEM_PIPELINES": {
            'ScrapyCrawler.pipelines.WxappPipeline': 300,
        }
    }

    rules = (
        # allow: 允许提取满足这个规则的链接
        # callback: 当提取到了符合allow规则的链接,使用哪个函数去解析
        # follow: 默认值为True,当在爬取的页面中发现了符合allow规则的链接,是否继续跟进
        # Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=\d'), follow=True),
        # Rule(LinkExtractor(allow=r'.+article-.+\.html'),
        #      callback='parse_datail', follow=False),
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/article-.+\.html'),
             callback='parse_datail', follow=False),
    )

    def parse_datail(self, response):
        # 爬取微信小程序详情页面的标题
        # print(type(response.xpath('//h1[@class="ph"]/text()')))
        title = response.xpath('//h1[@class="ph"]/text()').extract_first()
        author = response.xpath('//p[@class="authors"]/a/text()').extract_first()
        pubdate = response.xpath('//span[@class="time"]/text()').extract_first()
        content = response.xpath('//td[@id="article_content"]//text()').extract()  # 得到是一个列表类型的数据
        content = "".join(content).strip()  # 把列表类型数据转成成字符串类型,并去除两端的空格
        print(title,author,pubdate)
        # print(content)
        wxappItem = WxappItem(title=title,author=author,pubdate=pubdate,content=content)
        yield wxappItem

