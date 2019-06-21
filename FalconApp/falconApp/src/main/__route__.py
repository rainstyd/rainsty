#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   __route__.py
@time:   2019-06-21 10:05
@description:
"""

from . import app
from .main import *

app.add_route('/main', Main())
