# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
CREATE TABLE `lico_mo_dshjs` (
  `EID` decimal(18,0) NOT NULL,
  `ESEQID` decimal(29,0) NOT NULL,
  `EITIME` datetime NOT NULL,
  `EUTIME` datetime NOT NULL,
  `EGETTIME` datetime NOT NULL,
  `EISDEL` char(1) COLLATE utf8_bin DEFAULT '0',
  `NOTICEDATE` datetime DEFAULT NULL,
  `REMARK` text COLLATE utf8_bin,
  `RANK` decimal(20,8) DEFAULT NULL,
  `ENDDATE` datetime DEFAULT NULL,
  `PASSNOTICEDATE` datetime DEFAULT NULL,
  `SESS` decimal(20,8) DEFAULT NULL,
  `NOMIDATE` datetime DEFAULT NULL,
  `UPDATEDATE` datetime DEFAULT NULL,
  `STARTDATE` datetime DEFAULT NULL,
  `PASSNOMIDATE` datetime DEFAULT NULL,
  `REASONREMARK` text COLLATE utf8_bin,
  `PERSONTYPE` varchar(24) COLLATE utf8_bin DEFAULT NULL,
  `COMPANYCODE` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `POSTCODE` varchar(40) COLLATE utf8_bin DEFAULT NULL,
  `REASON` varchar(80) COLLATE utf8_bin DEFAULT NULL,
  `STATUS` varchar(80) COLLATE utf8_bin DEFAULT NULL,
  `PERSONCODE` varchar(80) COLLATE utf8_bin DEFAULT NULL,
  `ESOURCEMEMO` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `PERSONNAME` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `POST` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`EID`),
  KEY `EM_LICO_MO_DSHJS` (`EISDEL`,`ESEQID`,`EGETTIME`,`EUTIME`),
  KEY `PK_LG_LICO_MO_DSHJS` (`COMPANYCODE`,`PERSONTYPE`,`SESS`,`POST`,`PERSONCODE`,`PASSNOMIDATE`,`STARTDATE`,`STATUS`),
  KEY `idx_lico_mo_dshjs_eutime` (`EUTIME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin ROW_FORMAT=DYNAMIC COMMENT='董事和监事'
"""


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
