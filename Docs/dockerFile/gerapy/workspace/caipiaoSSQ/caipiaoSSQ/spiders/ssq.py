# -*- coding: utf-8 -*-
import scrapy
import re
from caipiaoSSQ.items import CaipiaossqItem


class SsqSpider(scrapy.Spider):
    name = 'ssq'
    # allowed_domains = ['17500.cn']
    # start_urls = ['http://www.17500.cn/ssq/awardlist.php?p=1']
    # print(start_urls[0])

    url_set = set()

    def start_requests(self):
        url = 'http://www.17500.cn/ssq/awardlist.php?p=1'
        SsqSpider.url_set.add(url)
        yield self.make_requests_from_url(url)

    def parse(self, response):

        allSSQ = response.css('table.sortable')

        file_name = ['期号', '日期', '周', '开奖号码', '本期投注', '返奖比', '奖池金额', '一等奖', '奖金一',
             '二等奖', '奖金二', '三等奖', '奖金三', '四等奖', '奖金四', '五等奖', '奖金五', '六等奖', '奖金六']

        file_value = []
        for t in allSSQ:
            for ta in t.xpath('./tbody/tr/td').extract():
                ta = re.sub('<td>|</td>|<span class="r">|</span>', '', ta)
                file_value.append(ta)

        file_result = []
        item = CaipiaossqItem()
        for l in range(len(file_value)):
            file_result.append(file_value[l])
            if (l + 1) % 19 == 0:
                item['name'] = dict(zip(file_name, file_result))
                yield item
                file_result = []

        page_num = ''
        for p in response.xpath('//div[contains(@id,"sortlist")]/a').extract():
            if '下一页' in p:
                page_num = p
                break

        try:
            page = re.findall('\"?p=(.*)\"', page_num)
            if page and len(page) > 0:
                page = page[0]
                url = 'http://www.17500.cn/ssq/awardlist.php?p=%s' % str(page)
                print(url)
                if url in SsqSpider.url_set:
                    pass
                else:
                    SsqSpider.url_set.add(url)
                    yield self.make_requests_from_url(url)
        except BaseException as e:
            print("这是错误: {}".format(e))

