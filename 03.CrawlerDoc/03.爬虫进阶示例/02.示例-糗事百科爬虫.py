# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-01-12 15:13

# https://www.qiushibaike.com/text/page/2/
import requests
from lxml import etree
import json


class QiushiSpider(object):

    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/text/page/{}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}

    def get_url_list(self):
        url_list = [self.start_url.format(i) for i in range(1,14)]
        return url_list

    def parse_url(self, url):  # 2.发送请求,获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):  # 3.提取数据
        html = etree.HTML(html_str)
        html__list = html.xpath('//div[@id="content-left"]/div')
        # print(len(content_list),content_list)
        content_list = []
        for content in html__list:
            html_dict = {}
            html_dict['user_url'] = content.xpath('./div[@class="author clearfix"]/a[2]/@href')
            # print(type(html_dict['user_url']))
            html_dict['user_name'] = content.xpath('./div[@class="author clearfix"]/a[2]/h2/text()')
            # print(type(html_dict['user_name']))
            html_dict['user_text_url'] = content.xpath('./a[1]/@href')
            # print(type(html_dict['user_text_url']))
            html_dict['user_text'] = content.xpath('./a[1]//span/text()')
            # print(type(html_dict['user_text']))
            # print(html_dict)
            content_list.append(html_dict)
        # next_url = html.xpath('//ul[@class="pagination"]/li[8]/a/@href')[0] if \
        # html.xpath('//span[@class="next"]/text()')[0].strip() == "下一页" else None
        # next_url = html.xpath('//span[@class="next"]/text()')[0].strip()
        # print(next_url)
        return content_list

    def save_conten(self, content_list):  # 4.保存数据
        with open('qiushiu.json', 'a', encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")  # 换行
        print("保存成功...")

    def run(self):  # 实现业务逻辑
        # 1.url_list地址
        url_list = self.get_url_list()
        # 2.发送请求,获取响应
        for url in url_list:
            html_str = self.parse_url(self.start_url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存数据
            self.save_conten(content_list)

if __name__ == '__main__':
    qiushi = QiushiSpider()
    qiushi.run()
