#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   decimal_basis.py
@time:   2019-10-24 15:29:58
@description:
"""

"""
关于数据库对应的字段类型操作
"""
import decimal

import pymysql

config = dict(
    host='',
    port=3306,
    user='root',
    password='123456',
    database='',
    charset='utf8'
)
conn = pymysql.connect(**config)
cursor = conn.cursor()

sql = "select * from user limit 10"
cursor.execute(sql)

result = cursor.fetchall()
print(result)
cursor.close()
conn.close()

for r in result:
    for e in r:
        if isinstance(e, decimal.Decimal):
            print(e.quantize(decimal.Decimal('0.00')))
