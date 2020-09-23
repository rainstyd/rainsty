#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   config.py
@time:   2019-09-29 09:01
@description:
"""

import os


class Config(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class MainConfig(Config):
    SECRET_KEY = 'fj4si7fd3ak45h454yd9tr7hh75bfs7akj1b6k4bhf5f7bh5fh8khg9hg8b4k'
