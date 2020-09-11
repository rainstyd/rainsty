#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   configparser_basis.py
@time:   2019-10-24 15:00:15
@description:
"""

from configparser import ConfigParser
import os
import codecs
import chardet

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Test/file/config/config.ini')
conf = ConfigParser()

with open(config_file, 'rb') as rb:
    code = chardet.detect(rb.read())

print(code)

with codecs.open(config_file, 'r', encoding=code['encoding']) as r:
    # conf.readfp(r)
    conf.read_file(r)

sections = conf.sections()
print(sections)

config = dict(conf.items('config'))
print(config)
