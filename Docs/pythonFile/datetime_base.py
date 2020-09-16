#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   datetime_base.py
@time:   2019-10-24 14:16:44
@description:
"""

import time
import datetime

# 获取当前时间
now = datetime.datetime.now()
print(now)
print(type(now))

# 格式化时间为str
now = now.strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(type(now))

# 时间段转datetime
now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
print(now)
print(type(now))

# 日期计算
now = now + datetime.timedelta(days=10)
print(now)
print(type(now))

print(now.date())
print(now.time())
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 获取当前时间戳(s)
now = time.time()
print(now)
print(type(now))

# 时间戳转时间段(s)
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
print(now)
print(type(now))

# 时间段转时间戳(s)
now = time.mktime(time.strptime(now, '%Y-%m-%d %H:%M:%S'))
print(now)
print(type(now))
