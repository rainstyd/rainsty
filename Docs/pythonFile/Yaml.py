#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   Yaml.py
@time:   2020-09-17 20:33:29
@description:
"""

import yaml


with open('./file/config.yml', 'r') as r:
    temp = yaml.load(r.read(), Loader=yaml.FullLoader)

print(temp)
