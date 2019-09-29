#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   app.py
@time:   2019-09-29 08:50
@description:
"""

from flask import Flask
from .main import api as main


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def register_blueprint(app):
    app.register_blueprint(main, url_prefix='')
    return app
