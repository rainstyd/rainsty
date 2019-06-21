#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   test.py
@time:   2019-06-20 10:34
@description:
"""

import falcon


class ThingsResource(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        print(req)
        print(req.params)
        print(req.get_param('x'))
        print(req.get_param('z'))
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')
