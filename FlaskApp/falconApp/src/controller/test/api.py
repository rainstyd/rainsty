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
from src.code import msg


class TestMain(object):

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def on_get(self, req, resp):

        self.logger.info(req.body)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(dict(code=0, msg=msg[0], data={'a': 'b'}))

    def on_post(self, req, resp):

        self.logger.info(req.body)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(dict(code=0, msg=msg[0], data={'c': 'd'}))
