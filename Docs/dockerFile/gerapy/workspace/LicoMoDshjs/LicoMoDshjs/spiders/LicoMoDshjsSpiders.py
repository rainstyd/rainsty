# -*- coding: utf-8 -*-
import scrapy
import datetime
# from LicoMoDshjs.connect import MysqlConnect
from LicoMoDshjs.items import LicomodshjsItem
import json


class LicomodshjsspidersSpider(scrapy.Spider):
    name = 'LicoMoDshjsSpiders'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    # def get_stock_list(self):
    #     config = dict(
    #         host=getattr(self, 'host_s', ''),
    #         port=int(getattr(self, 'port_s', '')),
    #         user=getattr(self, 'user_s', ''),
    #         password=getattr(self, 'passwd_s', ''),
    #         database=getattr(self, 'db_s', ''),
    #         charset=getattr(self, 'charset', 'utf8'),
    #     )
    #     mc = MysqlConnect(config)
    #     mc.create_connect()
    #
    #     state, result = mc.get_data(sql="""
    #             SELECT
    #                 StockCode, comcode CODE,
    #                 CASE
    #                     WHEN F1102_032=83 THEN 'SH'
    #                     WHEN F1102_032=90 THEN 'SZ'
    #                 ELSE '' END Market
    #             FROM
    #                 jl_base_1102
    #             WHERE
    #                 F1102_022 = 1 AND F1102_031 = 1
    #                     AND F1102_032 IN (83 , 90)
    #             ORDER BY stockcode ASC
    #         """)
    #     if not state:
    #         print(result)
    #
    #     return result
    #
    # def get_post_code(self):
    #     config = dict(
    #         host=getattr(self, 'host_s', ''),
    #         port=int(getattr(self, 'port_s', '')),
    #         user=getattr(self, 'user_s', ''),
    #         password=getattr(self, 'passwd_s', ''),
    #         database=getattr(self, 'db_s', ''),
    #     )
    #     mc = MysqlConnect(config)
    #     mc.create_connect()
    #
    #     state, result = mc.get_data(
    #         sql="select Code, Name from jlzx.jl_base_1002 where typecode='1026'")
    #
    #     if not state:
    #         print(result)
    #
    #     return result
    #
    # def update_data(self, code):
    #     config = dict(
    #         host=getattr(self, 'host', ''),
    #         port=int(getattr(self, 'port', '')),
    #         user=getattr(self, 'user', ''),
    #         password=getattr(self, 'passwd', ''),
    #         database=getattr(self, 'db', ''),
    #     )
    #     mc = MysqlConnect(config)
    #     mc.create_connect()
    #
    #     state, result = mc.exec_cmd(
    #         sql="""update {}.lico_mo_dshjs set EISDEL='1' where COMPANYCODE='{}'""".format(
    #             config['database'], code))
    #     if not state:
    #         print(result)
    #     else:
    #         mc.close_connect()
    #         print(
    #             '-------------------------------update success---------------------------------------')

    def init_before_action(self):
        """
        初始化三个全局变量，作为实例属性
        """
        # self.stock_list = self.get_stock_list()
        # self.stock_dict = {}
        # for stock_data in self.stock_list:
        #     self.stock_dict[str(stock_data.get('StockCode'))
        #                     ] = stock_data.get('CODE')
        # self.post_code = self.get_post_code()
        # self.post_code_dict = {}
        # for code in self.post_code:
        #     self.post_code_dict[str(code.get('Name'))] = code.get('Code')

        self.stock_list = [dict(StockCode='000001', Market='SZ')]

    def start_requests(self):

        self.init_before_action()

        for stock_data in self.stock_list:
            url = "http://f10.eastmoney.com/CompanyManagement/CompanyManagementAjax?code={}{}".format(
                stock_data['Market'], stock_data['StockCode'])
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            }

            yield scrapy.Request(url, callback=self.parse_without_selenium, headers=headers, meta={"stockcode": stock_data['StockCode']})

    person_type_dict = {
        # "董事会":"01",
        # "监事会":"02",
        "战略委员会": "03",
        "审计委员会": "04",
        "提名委员会": "05",
        "薪酬与考核委员会": "06",
        "研究发展委员会": "07",
        "资产管理委员会": "08",
        "执行委员会": "09",
        "人力资源委员会": "21",
        "财务委员会": "22",
        "专家委员会": "23",
        "基本建设及技术改造委员会": "24",
        "决策与咨询委员会": "25",
        "定价委员会": "26",
        "预算委员会委员": "27",
        "风险管理委员会": "28",
        "协联会委员会": "29",
        "行业规划与业态创新指导委员会": "30",
    }

    def get_person_type(self, post):
        """
        根据职务判定董监类型
        """
        if '董事' in post:
            return '01'
        elif '监事' in post:
            return '02'
        else:
            for key, value in self.person_type_dict.items():
                if post in key:
                    return value

    def parse_without_selenium(self, response):
        stock_code = response.meta.get('stockcode')
        if '代码不合法' in response.text:
            print("stock code is unvalid：{}".format(stock_code))
            return
        json_data = json.loads(response.text)
        # print(json_data)
        rank = 0
        # company_code = self.stock_dict.get(stock_code)
        # self.update_data(company_code)
        company_code = '4d7e472eeb8b11eb806e0242ac190003'
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
            item["COMPANYCODE"] = company_code
            item["POSTCODE"] = post.split(',')[0]
            item["REASON"] = None
            item["STATUS"] = '2'
            item["PERSONCODE"] = None
            item["ESOURCEMEMO"] = None
            item["PERSONNAME"] = manager['xm']
            item["POST"] = post
            yield item
