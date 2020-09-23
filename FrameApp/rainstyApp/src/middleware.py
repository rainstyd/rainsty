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
from .code import msg


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
                if req.path == self.config.route_path + '/reqxml':
                    req.path = self.config.route_path + '/reqxml' + '/' + req.body.get('action')
                # self.logger.info(req.path)
                # self.logger.info(req.body)

            except (ValueError, UnicodeDecodeError):
                raise UserHttpError(description=dict(code=3005, msg=msg[3005]))

        elif req.method in ('POST', 'PUT', 'DELETE'):
            body = req.stream.read()
            if not body:
                # 检查请求内容是否支持json，编码是否支持utf-8
                raise UserHttpError(description=dict(code=3004, msg=msg[3004]))
            try:
                # 后续请求参数全部放入req.body中
                req.body = json.loads(body.decode('utf-8'))
                if req.path == self.config.route_path + '/reqxml':
                    req.path = self.config.route_path + '/reqxml' + '/' + req.body.get('action')
                # self.logger.info(req.path)
                # self.logger.info(req.body)

            except (ValueError, UnicodeDecodeError):
                raise UserHttpError(description=dict(code=3005, msg=msg[3005]))
