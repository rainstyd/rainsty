#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   middleware.py
@time:   2019-12-30 13:32:29
@description: middleware
"""

import falcon
import json
from src.code import msg
from src.models.user import User
from src.models import db_session
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class UserHttpError(falcon.HTTPError):
    """User Http Error"""

    def __init__(self, title=None, description=None, headers=None, status_code=falcon.status.HTTP_200, **kwargs):
        super(UserHttpError, self).__init__(status_code, title, description, headers, **kwargs)

    def to_dict(self, obj_type=dict):
        obj = obj_type()

        if self.description:
            obj['code'] = self.description.get('code')
            obj['msg'] = self.description.get('msg')
            if self.description.get('token'):
                obj['token'] = self.description.get('token')
        else:
            obj['code'] = 4000
            obj['msg'] = msg[4000]

        return obj


class AuthRequest(object):
    """Auth Request"""

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def process_request(self, req, resp):
        self.logger.info((req.forwarded_host, req.port, req.method, req.path, resp.status, resp.body))

        if not req.client_accepts_json:
            # 检查client_accepts_json是否支持json
            raise UserHttpError(description=dict(code=3003, msg=msg[3003]))

        if req.content_type and 'application/json' not in req.content_type:
            # 检查content_type是否为application/json
            raise UserHttpError(description=dict(code=3003, msg=msg[3003]))

        if req.method in ('GET',):
            body = req.params
            try:
                # 后续请求参数全部放入req.body中
                req.body = json.loads(json.dumps(body).encode('utf-8').decode('utf-8'))

            except (ValueError, UnicodeDecodeError):
                raise UserHttpError(description=dict(code=3005, msg=msg[3005]))

        elif req.method in ('POST', 'PUT', 'DELETE'):
            # 检查请求内容是否支持json，编码是否支持utf-8
            body = req.stream.read()
            if not body:
                raise UserHttpError(description=dict(code=3004, msg=msg[3004]))
            try:
                # 后续请求参数全部放入req.body中
                req.body = json.loads(body.decode('utf-8'))

            except (ValueError, UnicodeDecodeError):
                raise UserHttpError(description=dict(code=3005, msg=msg[3005]))


class AuthToken(object):
    """Auth Token"""

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def path_filter(self, req, resp):
        if req.path == '/' and req.method == 'GET':
            # 首页
            raise UserHttpError(description=dict(code=0, msg='hello, world!'))

        elif req.path == '{}/login'.format(self.config.route_path) and req.method == 'POST':
            # 登录
            username = req.body.get('username', None)
            password = req.body.get('password', None)

            if not username or not password:
                raise UserHttpError(description=dict(code=3000, msg=msg[3000]))

            self.logger.info('user: {} is logging in......'.format(username))

            if not db_session.query(User).filter(User.username == username, User.password == password).first():
                raise UserHttpError(description=dict(code=3001, msg=msg[3001]))
            else:
                token_dict = dict(username=username, forwarded_host=req.forwarded_host)
                token = Serializer(self.config.SECRET_KEY, expires_in=7200).dumps(token_dict)
                self.logger.info((username, req.forwarded_host, req.port, req.method, req.path, resp.status, resp.body))
                raise UserHttpError(description=dict(code=0, msg=msg[0], token=token.decode('utf-8')))

        elif req.path == '{}/logout'.format(self.config.route_path) and req.method == 'POST':
            # 退出
            raise UserHttpError(description=dict(code=0, msg=msg[0]))

    def process_request(self, req, resp):
        # 过滤path
        self.path_filter(req, resp)

        # 验证token
        try:
            token = Serializer(self.config.SECRET_KEY).loads(req.get_header('Http-Authorization', ''))
            username = token.get('username')
            forwarded_host = token.get('forwarded_host')
            req.user = dict(username=username, forwarded_host=forwarded_host)

            self.logger.info((username, req.forwarded_host, req.port, req.method, req.path, resp.status, resp.body))
            return
        except (BaseException, Exception):
            raise UserHttpError(description=dict(code=3002, msg=msg[3002]))
