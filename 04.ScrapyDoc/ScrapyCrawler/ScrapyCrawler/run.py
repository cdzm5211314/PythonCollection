# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-04-01 16:16

from scrapy.cmdline import execute

# 执行爬虫文件方式:
# execute(["scrapy","crawl","爬虫名称"])
# execute("scrapy crawl 爬虫名称".split())

# execute("scrapy crawl qsbk --nolog".split())
# execute("scrapy crawl qsbk2 --nolog".split())
# execute("scrapy crawl wxapp --nolog".split())
# execute("scrapy crawl renren --nolog".split())
# execute("scrapy crawl bmw1 --nolog".split())
# execute("scrapy crawl bmw2 --nolog".split())
execute("scrapy crawl bmw3".split())

