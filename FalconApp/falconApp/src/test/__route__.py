#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   route.py
@time:   2019-06-21 10:05
@description:
"""

from . import app
from .test import ThingsResource

app.add_route('/test', ThingsResource())
