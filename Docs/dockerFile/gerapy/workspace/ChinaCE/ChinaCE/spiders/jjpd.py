import scrapy


class JjpdSpider(scrapy.Spider):
    name = 'jjpd'
    allowed_domains = ['http://finance.ce.cn/jjpd/index.shtml']
    start_urls = ['http://http://finance.ce.cn/jjpd/index.shtml/']

    def parse(self, response):
        pass
