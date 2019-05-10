# -*- coding:utf-8 -*-
# @Desc : 百度贴吧
# @Author : Administrator
# @Date : 2019-01-03 18:33

import requests


class TiebaSpider(object):

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.tieba_url = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}

    def get_url_list(self,num):  # 1.构造url列表
        # urllist = []
        # for i in range(num):
        #     urllist.append(self.tieba_url.format(i * 50))
        # return urllist
        return [self.tieba_url.format(i*50) for i in range(num)]

    def parse_url(self,url):  # 发送请求,获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode('utf-8')

    def save_html(self,html_str,page_num):  # 保存html字符串
        file_path = '{}-第{}页.html'.format(self.tieba_name,page_num)
        with open(file_path,'w',encoding="utf-8") as f:  # 月球-第3页.html
            f.write(html_str)

    def run(self,num):  # 实现主要逻辑
        # 1.构造url列表
        urllist = self.get_url_list(num)
        # 2.遍历,发送请求,获取响应
        for url in urllist:
            html_str = self.parse_url(url)
            # 3.保存数据
            page_num = urllist.index(url) + 1  # 页码数
            self.save_html(html_str,page_num)

if __name__ == '__main__':
    tiebaSpider = TiebaSpider("月球")
    tiebaSpider.run(3)



