# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # 爬虫一开始就发送POST请求,需要复写start_request(self)方法
    def start_requests(self):
        login_url = "http://www.renren.com/PLogin.do"
        login_data = {
            'email': '18103763930',
            'password': '****123456'
        }
        yield scrapy.FormRequest(login_url,formdata=login_data,callback=self.parse_page)

    def parse_page(self,response):
        # 测试是否登录成功
        # with open("renren.html","w",encoding="utf-8") as fp:
        #     fp.write(response.text)
        # 登录后访问的页面
        login_after_url = 'http://www.renren.com/893394172/profile'
        yield scrapy.Request(login_after_url,callback=self.parse_info)

    def parse_info(self,response):
        author = response.xpath("//h1[@class='avatar_title no_auth']/text()").extract_first().strip()
        print(author)


