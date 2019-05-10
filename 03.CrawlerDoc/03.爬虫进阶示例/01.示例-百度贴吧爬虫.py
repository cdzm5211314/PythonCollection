# -*- coding:utf-8 -*-
# @Desc : 使用浏览器模拟手机端
# @Author : Administrator
# @Date : 2019-01-10 18:46

# https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BC%96%E7%A8%8B&pn=200

import requests
from lxml import etree

class TiebaSpider(object):

    def __init__(self, tieba_name):
        self.url_temp = "https://tieba.baidu.com/f?ie=utf-8&kw=" + tieba_name + "&pn={}"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36'}

    def parse_url(self,url):  # 发送请求,获取响应
        print(url)
        response = requests.get(url,headers = self.headers)
        return response.content.decode('utf-8')

    def get_content_list(self,html_str):  # 提取数据
        e = etree.HTML(html_str)
        title_list = e.xpath('//li[@class="tl_shadow tl_shadow_new "]')
        # print(title_list)
        # content_list = e.xpath('//div[@class="ti_title"]/span/text()')
        # 提取下一页地址失败...
        next_url = e.xpath('//a[@class="j_pager_next bottom_pager_btn pager_next active"]')
        print(next_url,type(next_url))
        content_list = []
        for title in title_list:
            item = {}
            item['href'] = title.xpath("./a/@href")
            item['title'] = title.xpath('.//div[@class="ti_title"]/span/text()')
            content_list.append(item)
        # print(content_list,len(content_list))

        return content_list,next_url

    def save_content(self,content_list):  # 保存数据
        # with open("tiebatitle.txt",'a',encoding="utf-8") as f:
        #     for title in content_list:
        #         f.write(title)
        #         f.write('\n')  # 换行
        # 使用json
        import json
        with open("tiebatitle.txt",'a',encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')  # 换行
        print("保存成功...")

    def run(self):  # 实现爬虫的主要逻辑
        # 1.start_url
        url = self.url_temp.format(0)
        # 2.发送请求,获取响应
        html_str = self.parse_url(url)
        # 3.提取数据,获取下一页的url
        content_list,next_url = self.get_content_list(html_str)
        # 4.保存数据
        self.save_content(content_list)
        # 5.请求下一页url地址,进入循环

if __name__ == '__main__':
    tieba = TiebaSpider("编程")
    tieba.run()
