#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   route.py
@time:   2019-06-21 10:05
@description:
"""

from . import app
from .main import ThingsResource

app.add_route('/main', ThingsResource())
