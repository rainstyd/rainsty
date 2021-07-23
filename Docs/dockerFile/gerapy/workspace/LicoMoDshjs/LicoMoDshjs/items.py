# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LicomodshjsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    EID = scrapy.Field()
    ESEQID = scrapy.Field()
    EITIME = scrapy.Field()
    EUTIME = scrapy.Field()
    EGETTIME = scrapy.Field()
    EISDEL = scrapy.Field()
    NOTICEDATE = scrapy.Field()
    REMARK = scrapy.Field()
    RANK = scrapy.Field()
    ENDDATE = scrapy.Field()
    PASSNOTICEDATE = scrapy.Field()
    SESS = scrapy.Field()
    NOMIDATE = scrapy.Field()
    UPDATEDATE = scrapy.Field()
    STARTDATE = scrapy.Field()
    PASSNOMIDATE = scrapy.Field()
    REASONREMARK = scrapy.Field()
    PERSONTYPE = scrapy.Field()
    COMPANYCODE = scrapy.Field()
    POSTCODE = scrapy.Field()
    REASON = scrapy.Field()
    STATUS = scrapy.Field()
    PERSONCODE = scrapy.Field()
    ESOURCEMEMO = scrapy.Field()
    PERSONNAME = scrapy.Field()
    POST = scrapy.Field()
