# -*- coding: utf-8 -*-
import scrapy


class SsqSpider(scrapy.Spider):
    name = 'ssq'
    allowed_domains = ['17500.cn']
    start_urls = ['http://17500.cn/']

    def parse(self, response):
        pass
