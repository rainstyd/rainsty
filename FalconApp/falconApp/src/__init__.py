#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   __init__.py
@time:   2019-06-21 11:15
@description:
"""

from falcon_manage import app
from .main.route import app
from .test.route import app