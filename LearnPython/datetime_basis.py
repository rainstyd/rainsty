#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   datetime_basis.py
@time:   2019-10-24 14:16:44
@description:
"""

import datetime
import time

# datetime
n = datetime.datetime.now()
print(n)
print(n.__class__)

n1 = n.strftime('%Y-%m-%d %H:%M:%S')
print(n1)
print(n1.__class__)

n2 = datetime.datetime.strptime(n1, '%Y-%m-%d %H:%M:%S')
print(n2)
print(n2.__class__)

n3 = time.time()
print(n3)
print(n3.__class__)

n4 = time.strptime(n1, '%Y-%m-%d %H:%M:%S')
n4 = time.mktime(n4)
print(n4)
print(n4.__class__)

n5 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(n3)))
print(n5)
print(n5.__class__)

