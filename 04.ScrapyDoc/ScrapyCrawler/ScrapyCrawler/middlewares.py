# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ScrapycrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapycrawlerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 设置随机请求头中间件:
import  random
# print( random.random() )             # 产生 0 到 1 之间的随机浮点数
# print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
# print( random.choice('tomorrow') )   # 从序列中随机选取一个元素

# fake_useragent模块可以生成随机的User-Agent
class UserAgentDownloaderMiddleware(object):

    # 定义一个User-Agent的列表
    USER_AGENT = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
    ]

    def process_request(self,request,spider):
        # 从列表中随机获取一个元素
        user_agent = random.choice(self.USER_AGENT)
        request.headers['User-Agent'] = user_agent

# 设置动态IP代理中间件:
class ProxyDownloaderMiddleware(object):

    # 定义一个IP地址列表
    PROXIES = [
        '122.193.244.243:9999',
        '111.77.196.121:9999',
        '112.85.164.189:9999',
        '110.52.235.244:9999',
        '171.41.82.167:9999'
    ]

    def process_request(self,request,spider):
        # request.meta['proxy'] = "http://ip:port"
        # request.meta['proxy'] = "http://username:password@ip:port"
        # request.meta['proxy'] = "http://175.165.128.214:1133"
        request.meta['proxy'] = random.choice(self.PROXIES)
        # 或者使用账号密码,如下
        # import base64
        # userandpassword = "user:password"
        # b64_userandpassword = base64.b64encode(userandpassword.encode("utf-8"))
        # request.headers['Proxy-Authorization'] = 'Basic' + b64_userandpassword.decode("utf-8")

        # ipproxy = "171.41.82.167:9999"
        # request.headers["proxy"] = ipproxy

