#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   Configparser.py
@time:   2020-09-17 20:23:29
@description:
"""

import codecs
import chardet
import configparser


config_file = './file/config.ini'
conf = configparser.ConfigParser()

# 获取文件编码
with open(config_file, 'rb') as rb:
    code = chardet.detect(rb.read())

print(code)

# 以获取到的编码打开文件
with codecs.open(config_file, 'r', encoding=code['encoding']) as r:
    conf.read_file(r)

# 读取配置文件内容
# sections = conf.sections()
# print(sections)
# config = dict(conf.items('config'))
# print(config)

print(configparser.ConfigParser.getboolean(conf, 'config', 'sex'))

print(type(dict(conf['DEFAULT'])))
print(dict(conf['DEFAULT']))
print(list(conf.keys()))