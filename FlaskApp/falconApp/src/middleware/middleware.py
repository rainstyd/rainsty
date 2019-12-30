#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   middleware.py
@time:   2019-12-30 13:32:29
@description: middleware
"""

import falcon


class AuthMiddleware(object):

    def __init__(self, config):
        self.config = config
        self.logger = self.config.logger

    def process_request(self, req, resp):
        # token = req.get_header('Authorization')
        # account_id = req.get_header('Account-ID')

        # challenges = ['Token type="Fernet"']
        self.logger.info((req, resp, falcon.HTTP_200))

    #     if token is None:
    #         description = ('Please provide an auth token '
    #                        'as part of the request.')
    #
    #         raise falcon.HTTPUnauthorized('Auth token required',
    #                                       description,
    #                                       challenges,
    #                                       href='http://docs.example.com/auth')
    #
    #     if not self._token_is_valid(token, account_id):
    #         description = ('The provided auth token is not valid. '
    #                        'Please request a new token and try again.')
    #
    #         raise falcon.HTTPUnauthorized('Authentication required',
    #                                       description,
    #                                       challenges,
    #                                       href='http://docs.example.com/auth')
    #
    # def _token_is_valid(self, token, account_id):
    #     return True  # Suuuuuure it's valid...
