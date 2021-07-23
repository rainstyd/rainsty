# -*- coding: utf-8 -*-
import scrapy
import datetime
import json
from LicoMoDshjs.items import LicomodshjsItem


class LicomodshjsspidersSpider(scrapy.Spider):
    name = 'LicoMoDshjsSpiders'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    def init_before_action(self):

        self.stock_list = [dict(StockCode='000001', Market='SZ'), dict(StockCode='600600', Market='SH')]

    def start_requests(self):

        self.init_before_action()

        for stock_data in self.stock_list:

            url = "http://f10.eastmoney.com/CompanyManagement/CompanyManagementAjax?code={}{}"
            url = url.format(stock_data['Market'], stock_data['StockCode'])

            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            }

            yield scrapy.Request(url, callback=self.callback, headers=headers, meta={"StockCode": stock_data['StockCode']})

    def callback(self, response):
        stock_code = response.meta.get('StockCode')

        if '代码不合法' in response.text:
            self.logger.error("stock code is unvalid：{}".format(stock_code))
            return

        json_data = json.loads(response.text)
        rank = 0

        for manager in json_data['RptManagerList']:
            rank += 1
            eid = int('10000000' + stock_code) * 10000 + rank
            now_time = datetime.datetime.now()
            post = manager['zw']
            item = LicomodshjsItem()
            item["EID"] = eid
            item["ESEQID"] = eid
            item["EITIME"] = now_time
            item["EUTIME"] = now_time
            item["EGETTIME"] = now_time
            item["EISDEL"] = '0'
            item["NOTICEDATE"] = now_time
            item["REMARK"] = None
            item["RANK"] = rank
            item["ENDDATE"] = None
            item["PASSNOTICEDATE"] = None
            item["SESS"] = None
            item["NOMIDATE"] = None
            item["UPDATEDATE"] = None
            item["STARTDATE"] = manager['rzsj']
            item["PASSNOMIDATE"] = None
            item["REASONREMARK"] = None
            item["PERSONTYPE"] = post
            item["COMPANYCODE"] = '4d7e472eeb8b11eb806e0242ac190003'
            item["POSTCODE"] = post.split(',')[0]
            item["REASON"] = None
            item["STATUS"] = '2'
            item["PERSONCODE"] = None
            item["ESOURCEMEMO"] = None
            item["PERSONNAME"] = manager['xm']
            item["POST"] = post
            yield item
