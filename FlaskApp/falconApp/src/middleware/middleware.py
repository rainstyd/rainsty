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
        else:
            obj['code'] = 4000
            obj['msg'] = msg[4000]

        return obj


class AuthMiddleware(object):
    """Auth Middleware"""

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

        if req.path == '/' and req.method == 'GET':
            # 首页
            return

        elif req.path == '{}/login'.format(self.config.route_path) and req.method == 'POST':
            # 登录
            return

        elif req.path == '{}/logout'.format(self.config.route_path) and req.method == 'POST':
            # 退出
            return

        else:
            # 验证token
            try:
                token = req.get_header('Http-Authorization', '')
                agent = req.get_header('User-Agent', '').lower()
                self.logger.info((token, agent))
                s = Serializer(self.config.SECRET_KEY)
                s.loads(token).get('username')
                return
            except (BaseException, Exception):
                raise UserHttpError(description=dict(code=3002, msg=msg[3002]))
