#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   do_50000.py
@time:   2020-09-22 15:23:29
@description:
"""

import json
from py_module.agent import action


@action('50001')
def do_action(req, resp):

    print(req.path)
    print('aaaaaaa')
    resp.status = '200'
    resp.body = json.dumps(dict(code=0, msg='成功', data={'c': 'd'}))
