#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   api.py
@time:   2020-01-02 18:20:29
@description:
"""

import falcon
import json
from src.code import msg
from src.models.user import User
from src.models import db_session
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class UserLogin(object):

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def on_get(self, req, resp):
        # 首页
        self.logger.info(req.body)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(dict(code=0, msg='hello, world!'))

    def on_post(self, req, resp):
        # 登录
        username = req.body.get('username', None)
        password = req.body.get('password', None)

        if not username or not password:
            resp.body = json.dumps(dict(code=3000, msg=msg[3000]))

        self.logger.info('用户: {} 正在登录......'.format(username))
        if not db_session.query(User).filter(User.username == username, User.password == password).first():
            resp.body = json.dumps(dict(code=3001, msg=msg[3001]))
        else:
            token = Serializer(self.config.SECRET_KEY, expires_in=7200).dumps({'username': username})
            resp.body = json.dumps(dict(code=0, msg=msg[0], token=token.decode('utf-8')))
