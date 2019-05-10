# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyCrawler'

SPIDER_MODULES = ['ScrapyCrawler.spiders']
NEWSPIDER_MODULE = 'ScrapyCrawler.spiders'

# 设置日志的级别或者把日志信息存储到文件中
# 日志的级别(从高到低): CRITICAL(严重错误) ERROR(一般错误) WARNING(警告) INFO(一般信息) DEBUG(调试信息)[默认级别]
# 日志信息级别:
# LOG_LEVEL = "WARNING"
import datetime

# 获取当前时间current_time
CURRENT_TIME = datetime.datetime.now()
# 项目目录下新建log目录,以每天日期为日志文件名称:
LOG_FILE_PATH = 'log/scarpy_{}_{}_{}.log'.format(CURRENT_TIME.year, CURRENT_TIME.month, CURRENT_TIME.day)
# 日志信息的存储文件位置,设置后终端不会显示日志信息:
# LOG_FILE = LOG_FILE_PATH


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ScrapyCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 默认为True,设置成False拒绝遵守Robot协议[爬虫协议]
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 延迟时间(秒)爬取
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 使用默认请求头信息,模拟浏览器发送请求,添加User-Agent
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ScrapyCrawler.middlewares.ScrapycrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载器中间件
# DOWNLOADER_MIDDLEWARES = {
#    'ScrapyCrawler.middlewares.ScrapycrawlerDownloaderMiddleware': 543,
#    'ScrapyCrawler.middlewares.UserAgentDownloaderMiddleware': 543,
#    'ScrapyCrawler.middlewares.ProxyDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 开启pipeline,数值越小,权重越高
# ITEM_PIPELINES = {
#     'ScrapyCrawler.pipelines.ScrapycrawlerPipeline': 300,
#     'ScrapyCrawler.pipelines.QsbkPipeline': 300,
#     'scrapy.pipelines.images.ImagesPipeline': 1,
#     'ScrapyCrawler.pipelines.Bmw2Pipeline': 300,
#     'ScrapyCrawler.pipelines.Bmw3Pipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

### 为settings.py设置自定义属性
# 设置ImagesPipeline下载图片的存储位置路径
import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(BASE_PATH, 'images')
# 即: E:/workspace_PyCharm/WebCrawler/ScrapyCrawler/images
