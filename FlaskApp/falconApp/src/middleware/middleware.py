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


class AuthMiddleware(object):

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def process_request(self, req, resp):

        self.logger.info((req.forwarded_host, req.port, req.method, req.path, resp.status, resp.body))

        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.',
                href='http://docs.examples.com/api/json')

        if req.content_type and 'application/json' not in req.content_type:
            raise falcon.HTTPUnsupportedMediaType(
                'This API only supports requests encoded as JSON.',
                href='http://docs.examples.com/api/json')

        if req.method in ('POST', 'PUT', 'DELETE'):

            body = req.stream.read()
            if not body:
                raise falcon.HTTPBadRequest('Empty request body',
                                            'A valid JSON document is required.')
            try:
                req.body = json.loads(body.decode('utf-8'))

            except (ValueError, UnicodeDecodeError):
                raise falcon.HTTPError(falcon.HTTP_753,
                                       'Malformed JSON',
                                       'Could not decode the request body. The '
                                       'JSON was incorrect or not encoded as '
                                       'UTF-8.')

        if req.path == '/' and req.method == 'GET':
            return

        elif req.path == '{}/login'.format(self.config.route_path) and req.method == 'POST':
            return

        elif req.path == '{}/logout'.format(self.config.route_path) and req.method == 'POST':
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
            except BaseException as e:
                del e
                description = dict(code=3002, msg=msg[3002])
                raise falcon.HTTPUnauthorized('Http-Authentication required', description)
