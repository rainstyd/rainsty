#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   route.py
@time:   2019-12-30 15:22:29
@description:
"""

from src.controller.user import user
from src.controller.test import test


def add_route(app, config):

    # auth
    app.add_route('/', user.UserLogin(config))
    app.add_route(config.route_path + '/login', user.UserLogin(config))

    # /test
    app.add_route(config.route_path + '/test/main', test.TestMain(config))

    return app
