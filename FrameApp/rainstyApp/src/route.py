#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   route.py
@time:   2019-12-30 15:22:29
@description:
"""

from py_module.action import start_action
from py_module.agent import get_action_list
from .config import AppConfig


class TestMain(object):

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def on_get(self, req, resp):
        pass

    def on_post(self, req, resp):
        pass


def action_product(_func):

    test = TestMain(AppConfig)
    test.on_get = _func
    return test


def action_product_get(_func):

    test = TestMain(AppConfig)
    test.on_get = _func
    return test


def action_product_post(_func):

    test = TestMain(AppConfig)
    test.on_post = _func
    return test


def add_route(app, config):

    print(start_action)
    action_list = get_action_list()

    for action in action_list:
        if action['method'] == 'GET':
            func_action = action_product_get(action.get('class'))
        elif action['method'] == 'POST':
            func_action = action_product_post(action.get('class'))
        else:
            func_action = action_product(action.get('class'))

        func_path = config.route_path + '/reqxml/{}'.format(action.get('action'))
        print(func_path, func_action)
        app.add_route(func_path, func_action)

    return app
