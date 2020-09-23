#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   manage_app.py
@time:   2019-09-29 08:59
@description:
"""

from src.app import create_app, register_blueprint
from src.config import MainConfig

app = create_app(MainConfig)
app = register_blueprint(app)
