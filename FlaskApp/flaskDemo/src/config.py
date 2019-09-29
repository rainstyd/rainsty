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
    SECRET_KEY = 'fj4si7ak45hd9bfs7akj1b6k4b7b8k8b4k'
    RSA_KEY = 'fl9sfd8in3b6uib7vd7hau5eb9k1kj23054h6hub7bhd0alm'
