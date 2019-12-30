#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   api.py
@time:   2019-12-30 13:37:29
@description:
"""

import falcon
import json


class TestMain(object):

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def on_get(self, req, resp):

        self.logger.info(req)
        self.logger.info(req.params)
        # marker = req.get_param('marker') or ''
        # limit = req.get_param_as_int('limit') or 50

        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'a': 'b'})
