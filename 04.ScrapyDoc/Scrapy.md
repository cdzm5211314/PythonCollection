## 创建Scrapy爬虫项目
> scrapy startproject 项目名称  
## Scrapy项目目录结构:
```
|- scrapyproject: 项目根目录
    |- scrapyproject: 项目同名目录
        |- spiders: 项目的爬虫文件目录
            |- __init__.py
        |- __init__.py: 项目的初始化文件，用来对项目做初始化工作
        |- items.py: 项目的数据容器文件，用来定义要获取的数据
        |- middlewares.py: 项目的中间件文件
        |- pipelines.py: 项目的管道文件，用来对items中的数据进行进一步的加工处理
        |- settings.py: 项目的设置文件，包含了项目的设置信息
    |- scrapy.cfg: 项目的配置文件
```
## 创建真正的爬虫文件:
* 注:如果一个项目中有多个爬虫,爬虫名称必须是唯一  
* 创建基础的爬虫模版:  
> scrapy genspider -t basic 爬虫名称 爬虫网站域名: 
```基本爬虫文件基本内容:
class QsbkSpider(scrapy.Spider):
    name = 'qsbk' # 爬虫的名称(唯一)
    allowed_domains = ['qiushibaike.com']  # 允许爬虫爬取的域名
    start_urls = ['http://qiushibaike.com/']  # 开始爬取的网址
    def parse(self, response):  # 解析响应数据
        pass 
```  
* 创建自动的爬虫模版:
> scrapy genspider -t crawl 爬虫名称 爬虫网站域名: 
```自动爬虫文件基本内容:
class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']  # 允许的域名,只有在这个里面指定的域名的url才会被提取
    start_urls = ['http://qiushibaike.com/']
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
    # rules = (
    #   Rule(LinkExtractor(restrict_xpaths='//div[@class="bookname"]//a[4]'), callback='parse_item', follow=True),
    # )
    def parse_item(self, response):
        item = {}
        return item
        
LinkExtractor的参数详解: LinkExtractor就是url链接提取器，自动提取出来我们需要爬取的url链接
allow：允许的url，所有满足这个正则表达式的url都会被提取出来 　
deny：禁止的url,所有满足这个正则表达式的url都不会被提取出来
allowed_domains: 允许的域名,只有在这个里面指定的域名的url才会被提取
deny_domains: 禁止的域名,所有在这个里面指定的域名的url都不会被提取
restrict_xpaths：使用xpath表达式提取，和allow共同作用过滤链接
restrict_css: 使用css选择器提取,和allow共同作用过滤链接
tags=('a','area'): 接收一个标签(字符串)或一个标签列表,提取指定标签内的链接,
attrs=('href',): 默认提取tags里的href属性，也就是url链接。
unique: 默认值为True,是否应对提取的链接应用重复过滤。
strip: 默认值为True,是把地址前后多余的空格删除
deny_extensions: 默认值为None,排除非网页链接
process_value: 默认值为None,作用比较强大了,他接受一个函数,可以立即对提取到的地址做加工

Rule的参数详解: 如下
link_extractor: 一个LinkExtractor对象,用来定义爬虫规则
callback: 满足这个规则的url,应该要执行哪个回调函数,因为CrawlSpaider使用了parse作为回调函数,因此不要覆盖parse作为回调函数自己的回调函数
follow: 默认值为True,根据该规则从response中提取到的链接是否需要继续跟进
process_links: 从link_extractor中获取到链接后会传递到这个函数,用来过滤不需要爬取的链接

注: Rule无论有无callback，都由同一个_parse_response函数处理，只不过他会判断是否有follow和callback

``` 
## Spider爬虫获取数据的方法:  
> scrapy.selector.unified.SelectorList对象: `getall() == extract() , get() == extract_first()`     
> scrapy.selector.unified.Selector对象: `getall() == extract() , get() != extract_first()`     
 
## 测试执行爬虫文件:
* 终端命令行执行: scrpay crawl 爬虫文件 -o：后面是导出的文件名称 -t：后面是导出类型
> scrpay crawl 爬虫名称           # 有日志信息  
> scrpay crawl 爬虫名称 --nolog   # 无日志信息  
> scrpay crawl 爬虫名称 -o 文件名称 ---》 scrpay crawl qidian -o book.json   
> scrpay crawl 爬虫名称 -o 文件名称 ---》 scrpay crawl qidian -o book.csv  
* 编写测试文件执行爬虫文件: settings.py同级目录下创建一个文件:如 run.py文件,在此文件中编写:
```
from scrapy.cmdline import execute
# execute(["scrapy","crawl","爬虫名称","--nolog"])
# execute("scrapy crawl 爬虫名称 --nolog".split())
然后执行run.py文件,就是运行爬虫文件
```
* 注:测试爬虫文件可能报错:ModuleNotFoundError: No module named 'win32api'.需要安装模块:`pip install pypiwin32`
## Scrapy Shell: 终端测试数据提取
> 首先进入到Scrapy项目根目录  
> 然后`workon`到python虚拟环境  
> 使用`scrapy shell [url链接]`发起请求  
> 测试爬取的数据...  

## Scrapy项目添加日志文件信息: `settings.py`
```python
# 设置日志的级别或者把日志信息存储到文件中
# 日志的级别(从高到低): CRITICAL(严重错误) ERROR(一般错误) WARNING(警告) INFO(一般信息) DEBUG(调试信息)[默认级别]
# 日志信息级别:  
# LOG_LEVEL = "WARNING"  
# 以每天日期为日志文件名称  
import datetime  
# 获取当前时间current_time   
CURRENT_TIME = datetime.datetime.now()  
# 项目目录下新建log目录:  
LOG_FILE_PATH = 'log/scarpy_{}_{}_{}.log'.format(CURRENT_TIME.year,CURRENT_TIME.month,CURRENT_TIME.day)  
# 日志信息的存储文件位置,设置后终端不会显示日志信息:  
# LOG_FILE = LOG_FILE_PATH  
```

## 编写items的爬虫数据容器:  
* 1.编写一个类: 定义你爬虫文件需要提取的信息
```python
import scrapy
class QsbkItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()
```
* 2.在spider爬虫文件引入这个item类,并创建对象
```python
from ScrapyCrawler.items import QsbkItem
def parse(self, response):
    item = QsbkItem()
    item["author"] = response.xpath('.//div[@class = "author clearfix"]//img/@alt').extract_first()
    item["content"] = response.xpath('.//a//span/text()').extract_first().strip()  
    yield item  # 推送item数据到pipeline
    # 或者如下所写:
    # author = response.xpath('.//div[@class = "author clearfix"]//img/@alt').extract_first()
    # content = response.xpath('.//a//span/text()').extract_first().strip() 
    # item = QsbkItem(author = author,content = content)   
    # yield item
```

## 编写pipelines的爬虫数据处理: 数据存储到文件或数据库  
* 爬虫文件中使用`yield`只能推送`字典类型数据`和`item类型数据`到pipeline中
* 或者使用`return`一次返回所有的`item`到pipeline中
* `spider爬虫文件`可以配置自己单独的pipeline,这样数据就不会存储到其他的pipeline中
```python
# 1.在pipelines.py文件中编写一个spider文件对应的pipeline类
class QsbkPipeline(object):
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):
        return item
    def close_spider(self,spider):
        pass
# 注:pipeline类中有三个方法: 
# open_spider(): 开启爬虫时执行,只执行一次,可省略
# process_item(): 当爬虫有数据传送过来,就作处理
# close_spider(): 关闭爬虫时执行,只执行一次,可省略
# 2.在`spider爬虫文件`中设置如下信息: (数据不会存到其他的pipeline中)
    custom_settings = {
        "ITEM_PIPELINES": {
            'ScrapyCrawler.pipelines.QsbkPipeline': 300,
        }
    }
``` 
* 不设置spider爬虫独有的pipeline,只需在`setting.py`中设置开启pipeline:
```
ITEM_PIPELINES = {
   'ScrapyCrawler.pipelines.ScrapycrawlerPipeline': 300,
   'ScrapyCrawler.pipelines.QsbkPipeline': 200,
}
# 注: 在此为spider爬虫设置开启pipeline,数值越小,优先级越高(同时数据也会存到其他的pipeline中)
```  
* pipelines补充:
```python
from scrapy.exceptions import DropItem
class Day96Pipeline(object):

    def __init__(self,conn_str):
        self.conn_str = conn_str
        
    @classmethod
    def from_crawler(cls, crawler):
        # 初始化时候，用于创建pipeline对象
        conn_str = crawler.settings.get('DB')
        return cls(conn_str)

    def open_spider(self,spider):
        # 爬虫开始执行时，调用
        self.conn = open(self.conn_str, 'a')

    def close_spider(self,spider):
        # 爬虫关闭时，被调用
        self.conn.close()

    def process_item(self, item, spider):
        # 每当数据需要持久化时，就会被调用
        # if spider.name == 'chouti'
        tpl = "%s\n%s\n\n" %(item['title'],item['href'])
        self.conn.write(tpl)
        # 交给下一个pipeline处理
        return item
        # 丢弃item，不交给
        # raise DropItem()

"""
4个方法
crawler.settings.get('setting中的配置文件名称且必须大写')
process_item方法中，如果抛出异常DropItem表示终止，否则继续交给后续的pipeline处理
spider进行判断
"""
```
## Request与Response对象的讲解:
```python
## Request: 发送请求,参数详解
# url: request对象发送请求的url地址
# callback: 在下载器下载完相应的数据后执行的回到函数
# method: 请求方式,默认为`GET`方法,可以设置为其他方法
# headers: 请求头,对于一些固定的设置,可以放在`settings.py`文件中设置,对于非固定的,可以在发送请求时指定
# meta: 比较常用,用于在不同的请求之间传递数据时使用
# encoding: 编码,默认为`utf-8`,使用默认就可以了
# dot_filter: 默认为True,表示不由调度器过滤,在执行多次重复请求的时候用的比较多
# errback: 在发生错误的时候执行的函数

## Response: 由Scrapy自动构建,主要用来提取数据,属性详解
# text: 将返回来的数据作为`unicode`字符串返回
# body: 将返回来的数据作为`bytes`字符串返回
# xpath: 提取数据选择器
# css: 提取数据选择器
# meta: 从其他请求传递过来的`meta`属性,可以用来保持多个请求之间的数据连接
# encoding: 返回当前字符串编码和解码的格式

# 注: 1.如果我们请求数据的时候发送POST请求,需要使用Resquest子类FormRequest来实现
# 注: 2.如果我们在爬虫一开始就发送POST请求,需要在爬虫类中重写`start_request(self)`方法,并且不在调用start_url列表中的url

```

## 爬虫项目设置信息文件:settings.py
* robots.txt: 是遵循Robot协议的一个文件,保存在网站服务器中,作用是需要爬虫文件不能爬取本网站的哪些内容,默认是开启的  
* settings.py ---> ROBOTSTXT_OBEY = True ---> 设置成False,是拒绝遵守Robot协议  
* `settings.py`文件内置设置信息:
> 请求头信息(模拟客户端浏览器):
```python
USER_AGENT = 'ScrapyDemo (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
USER_AGENT = [
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
]
```
> 是否遵守爬虫规则: `ROBOTSTXT_OBEY = False`  
> 并发请求数(最大值为32): `CONCURRENT_REQUESTS = 32`  
> 下载延迟(秒): `DOWNLOAD_DELAY = 3`  
> 针对域名并发数: `CONCURRENT_REQUESTS_PER_DOMAIN = 16`  
> 针对IP并发数: `CONCURRENT_REQUESTS_PER_IP = 16`  
> 是否帮你爬取cookie: `COOKIES_ENABLED = False`  
> 默认的请求头信息,也可以添加User-Agent头信息:
```
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
```
* `settings.py`文件自定义设置信息:  
> DEPTH_LIMIT = 1  # 爬取深度  
> DEPTH_PRIORITY = 0 或 1  # 0表示深度优先(默认),1表示广度优先  
> 配置缓存策略:如下  
>> 是否启用缓存策略: `HTTPCACHE_ENABLED = True`  
>> 缓存策略：所有请求均缓存，下次在请求直接访问原来的缓存即可(默认):`HTTPCACHE_POLICY = "scrapy.extensions.httpcache.DummyPolicy"`  
>> 缓存策略：根据Http响应头：Cache-Control、Last-Modified 等进行缓存的策略:`HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"`  
>> 缓存超时时间:`HTTPCACHE_EXPIRATION_SECS = 0`  
>> 缓存保存路径: `HTTPCACHE_DIR = 'httpcache'`  
>> 缓存忽略的Http状态码: `HTTPCACHE_IGNORE_HTTP_CODES = []`  
>> 缓存存储的插件: `HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'`  

## xpath数据提取选择器:  
> /:    表示在子标签中查找  
> //:   表示在子孙标签中查找  
> .//:  表示当前对象的子孙标签中查找  
> /div: 表示子标签的div标签  
> //div:表示子孙中的所有div标签    
> /div[@class='name']:  表示子标签的div标签并且class属性值为name的  
> //div[@class='name']: 表示子孙标签的div标签并且class属性值为name的  
> //div/text():         表示所有子孙标签下的文本内容  
> obj.xpath("string(.)"): 表示取当前标签下的所有文本内容  
> obj.extract():          列表中的每一个对象转换为字符串  
> obj.extract_first():    获取列表中的第一个元素  
 > ''.join(obj.xpath("表达式").extract()): 将序列中的元素以指定的字符连接成一个新的字符串   

## 给url地址加密(已免URL地址过长):
```
import hashlib
def md5(self,url):
    obj = hashlib.md5()
    obj.update(bytes(url,encoding='utf-8'))
    return obj.hexdigest()
```

## 自动登陆: 用户名密码 + cookie
```
def parse(self,response):
    from scrapy.http.cookies import CookieJar
    cookie_obj = CookieJar()
    cookie_obj.extract_cookies(response,response.request)
    print(cookie_obj._cookies)  # 得到cookie的值
```

## 下载文件和图片的: FilesPipeline, ImagesPipeline
```python
## FilesPipeline: 自动下载文件
# 1. 定义一个Item,在Item中定义两个属性file_urls和files,file_urls用来存储需要下载的文件的url地址,是一个列表
# 2. 当文件下载完成后,会把文件的相关信息存储到Item的files属性中,如:下载路径,下载url和文件的校验码等
# 3. 在settings.py文件中添加属性设置: FILES_STORE ,用来设置文件下载下来的存储位置(本地)
# 4. 启动pipeline,在settings.py的ITEM_PIPELINES属性中添加: scrapy.pipelines.files.FilesPipeline:1

## ImagesPipeline: 自动下载图片
# 1. 定义一个Item,在Item中定义两个属性image_urls和images,image_urls用来存储需要下载的图片的url地址,是一个列表
# 2. 当图片下载完成后,会把图片的相关信息存储到Item的images属性中,如:下载路径,下载url和图片的校验码等
# 3. 在settings.py文件中添加属性设置: IMAGES_STORE ,用来设置图片下载下来的存储位置(本地)
# 4. 启动pipeline,在settings.py的ITEM_PIPELINES属性中添加: scrapy.pipelines.images.ImagesPipeline:1 

## 实现自定义分类下载图片,需要在pipelines.py文件中自定义pipeline类并继承ImagesPipeline
# 核心是重写: get_media_requests(self, item, info) 和 item_completed(self, results, item, info) 这2个方法
# 示例详情请见:WebCrawler\ScrapyCrawler\ScrapyCrawler\pipelines.py下的Bmw2Pipeline类

```
## 中间件分类: 下载器中间件(Downloader Middlewares) 和 爬虫中间件(Spider Middlewares)
```python
## 下载器中间件: Downloader Middlewares
# 下载器中间件: 是引擎和下载器之间通信的中间件,在这个中间件中科院设置IP代理,更换请求头等来达到反反爬虫的目的
# 下载器中间件核心实现两个方法:
# process_request(self,request,spider): 请求发送之前调用
# process_response(self,request,response,spider): 数据下载到引擎之前调用
# process_exception(self,request,exception,spider): 

## 爬虫中间件: Spider Middlewares
# process_spider_input(self,response,spider): 接收一个response对象并处理
# process_spider_output(self,response,result,spider): 当Spider处理response返回result时,该方法被调用
# process_spider_exception(self,response,exception,spider): spider出现的异常时被调用
# process_start_requests(self,start_requests,spider): 当spider发出请求时,被调用

```
## 中间件 - 随机请求头: 随机获取User-Agent
* 第一种固定写法:settings.py
```
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
```
* 第二种动态获取: `使用随机请求头中间件方式`
> 1.注销 setting:# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
> 2.在middlewares.py[文件中的内容可以清空]中编写一个类: 如 UserAgentDownloadMiddleware  
```
from fake_useragent import UserAgent
class UserAgentDownloaderMiddleware(object):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent',UserAgent().chrome)
        # request.headers.setdefault(b'User-Agent',UserAgent().random)
        # request.headers['User-Agent'] = UserAgent.random()
```
> 3.开启setting中的DOWNLOADER_MIDDLEWARES:
```
DOWNLOADER_MIDDLEWARES = {
   'ScrapyDemo.middlewares.UserAgentDownloaderMiddleware': 343, # 数字越小表示优先级越高
}
注:DOWNLOADER_MIDDLEWARES的middleware与上面编写的类一致,如果还是不能动态获取User-Agent,就调他的优先级,数字越小优先级越高
```
* 第三种动态获取:
> 1.setting中定义一个User-Agent的列表  
```
USER_AGENT = [
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
]
```
> 2.在middlewares.py[文件中的内容可以清空]中编写一个类: UserAgentDownloaderMiddleware
```
from ScrapyDemo.settings import USER_AGENT
from random import choice
class UserAgentDownloadMiddleware(object):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent',choice(settings.USER_AGENT))
```
> 3.开启setting中的DOWNLOADER_MIDDLEWARES:
```
DOWNLOADER_MIDDLEWARES = {
   'ScrapyDemo.middlewares.UserAgentDownloadMiddleware': 343, # 数字越小表示优先级越高
}
注:DOWNLOADER_MIDDLEWARES的middleware与上面编写的类一致,如果还是不能动态获取User-Agent,就调他的优先级,数字越小优先级越高
```

## 中间件 - 动态IP代理: 
* 1.创建一个文件[proxymiddlewares]编写一个类[Proxy],或者直接在middlewares.py文件中编写一个类[ProxyDownloaderMiddleware]
```
class ProxyDownloaderMiddleware(object):
def process_request(self, request, spider):
    # request.meta['proxy'] = "http://ip:port"
    # request.meta['proxy'] = "http://username:password@ip:port"
    request.meta['proxy'] = "http://175.165.128.214:1133"
```
* 2.开启中间件:setting  
```
DOWNLOADER_MIDDLEWARES = {
   'ScrapyDemo.proxymiddlewares.Proxy': 343,
   或者'ScrapyDemo.middlewares.ProxyDownloaderMiddleware': 343,
}

```
## Scrapy登录操作:
* 登陆方式一: 使用用户名与密码,爬虫文件一开始就发送POST请求 
> 1.注销: # start_urls = ['http://www.sxt.cn/index/user.html']  
> 2.重写start_requests方法,初始请求url:
```  
def start_requests(self):  
    # 登陆起始url  
    url = "http://www.sxt.cn/index/login/login.html"  
    # 账号和密码  
    form_data = {  
        "user" : "18103763930",  
        "password" : "18103763930"  
    }  
    # 发送登陆请求  
    yield scrapy.FormRequest(url,formdata=form_data,callback=self.parse)  
```
> 3.在爬虫文件的parse()方法中重新发送爬取请求  
```
def parse(self, response):
    # 重新发送请求,并编写一个解析方法
    yield scrapy.Request("http://www.sxt.cn/index/user.html",callback=self.parse_info)
```
> 4.重新编写解析方法
```
def parse_info(self,response):
    # 爬取的数据
    print(response.text)
```
* 登陆方式二: 携带cookie,cookie的类型是字典类型
> 1.在浏览器上获取登陆后页面的的cookie值  
```
cookie_str = "PHPSESSID=p2pq523v1ocd95gl7h7n…l; kf_72085067_land_page_ok=1"
```
> 2.在爬虫文件中重写start_requests()方法
```
# 注销 start_urls = ['http://www.sxt.cn/index/user.html']
def start_requests(self):
    cookie_str = "PHPSESSID=p2pq523v1ocd95gl7h7n…l; kf_72085067_land_page_ok=1"
    cookie_dict = {}
    for cookielist in cookie_str.split(';'):  # cookie_str.split(';') 根据;分号切割成列表形式
        key, value = cookielist.split("=")
        cookie_dict[key.strip()] = value.strip() # 去除空格
    yield scrapy.Request("http://www.sxt.cn/index/user.html",cookies=cookie_dict, callback=self.parse, )
```
> 3.解析爬取的数据
```
def parse(self, response):
    pass
```
* 登陆方式三: 登录数据 + 验证码
> 省略...

## scrapy_redis: 分布式爬虫

