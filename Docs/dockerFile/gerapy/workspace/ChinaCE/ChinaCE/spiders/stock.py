import scrapy


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['http://finance.ce.cn/stock/']
    start_urls = ['http://http://finance.ce.cn/stock//']

    def parse(self, response):
        pass
