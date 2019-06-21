#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   manage.py
@time:   2019-06-21 10:03
@description:
"""

from falcon import API
app = API()

# 注册route/url
from src import app
