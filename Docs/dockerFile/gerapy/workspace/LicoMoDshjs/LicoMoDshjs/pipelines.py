# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from LicoMoDshjs.connect import MysqlConnect


class LicomodshjsPipeline:
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        # self.conn = None
        pass

    def open_spider(self, spider):
        pass
        # try:
        #     config = dict(
        #         host=spider.host,
        #         port=int(spider.port),
        #         database=spider.db,
        #         user=spider.user,
        #         password=spider.passwd,
        #         charset=getattr(spider, 'charset', 'utf8'),
        #     )
        #     self.conn = MysqlConnect(config)
        #     self.conn.create_connect()
        # except BaseException as e:
        #     print(e)

    def process_item(self, item, spider):

        try:

            # sql_params = dict(item)
            #
            # insert_sql = """
            #         replace into {}.lico_mo_dshjs (
            #             EID, ESEQID, EITIME, EUTIME, EGETTIME, EISDEL, NOTICEDATE, REMARK, RANK, ENDDATE,
            #             PASSNOTICEDATE, SESS, NOMIDATE, UPDATEDATE, STARTDATE, PASSNOMIDATE, REASONREMARK,
            #             PERSONTYPE, COMPANYCODE, POSTCODE, REASON, STATUS, PERSONCODE, ESOURCEMEMO, PERSONNAME, POST
            #         ) values (
            #             %(EID)s, %(ESEQID)s, %(EITIME)s, %(EUTIME)s, %(EGETTIME)s, %(EISDEL)s, %(NOTICEDATE)s,
            #             %(REMARK)s, %(RANK)s, %(ENDDATE)s, %(PASSNOTICEDATE)s, %(SESS)s, %(NOMIDATE)s, %(UPDATEDATE)s,
            #             %(STARTDATE)s, %(PASSNOMIDATE)s, %(REASONREMARK)s, %(PERSONTYPE)s, %(COMPANYCODE)s,
            #             %(POSTCODE)s, %(REASON)s, %(STATUS)s, %(PERSONCODE)s, %(ESOURCEMEMO)s, %(PERSONNAME)s, %(POST)s
            #         )
            #     """.format(spider.db)
            #
            # state, error = self.conn.exec_cmd(sql=insert_sql, params=sql_params)

            # if not state:
            #     print('--------------error--------------{}'.format(error))
            # else:
            #     print('--------------info--------insert successful......')
            print(dict(item))

        except Exception as e:
            print(e)

        return item
