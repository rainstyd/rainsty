# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class CaipiaossqPipeline(object):
    def process_item(self, item, spider):
        with open("./my_ssq.txt",'a') as fp:
            fp.write(json.dumps(item['name'], ensure_ascii=False) + '\n')
