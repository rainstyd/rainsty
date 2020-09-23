#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   app.py
@time:   2019-12-30 13:21:29
@description:
"""

import falcon
from src.route import add_route
from src.middleware.middleware import AuthRequest, AuthToken


def create_app(config):
    app = falcon.API(middleware=[AuthRequest(config), AuthToken(config)])
    app.req_options.auto_parse_form_urlencoded = True
    app = add_route(app, config)

    return app
