# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-27 16:28

import requests
import re

def parse_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    # print(response.text)
    text = response.text
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>',text,re.DOTALL)  # 诗词名称
    # print(titles)
    dynastys = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)  # 朝代
    # print(dynastys)
    authors  = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)  # 作者
    # print(authors)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)  # 诗词内容
    contents = []  # 诗词内容列表
    for content in content_tags:
        tx = re.sub(r'<.*?>','',content)
        # print(tx.strip())
        contents.append(tx.strip())
    # print(contents)
    peoms = []
    for value in zip(titles,dynastys,authors,contents):
        title,dynasty,author,content = value
        # 诗词,朝代,作者,内容 组合成字典类型
        peom = {
            "title":title,
            "dynasty":dynasty,
            "author":author,
            "content":content
        }
        peoms.append(peom)

    for peom in peoms:
        print(peom)
        print("*"*30)

def run():
    base_url = "https://www.gushiwen.org/default_{}.aspx"
    for i in range(1,3):
        url = base_url.format(i)
        parse_page(url)

if __name__ == '__main__':
  run()





