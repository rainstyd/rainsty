#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   manage_app.py
@time:   2019-12-30 13:21:29
@description:
"""

from src.app import create_app
from src.config import AppConfig


app = create_app(AppConfig)
