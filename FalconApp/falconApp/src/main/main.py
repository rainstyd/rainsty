#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   main.py
@time:   2019-06-20 10:34
@description:
"""

import falcon


class Main(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status

        resp.body = """
            <form>
              <input id="text" type="text" size="40" placeholder="Enter Text">
              <button id="button" name="synthesize">Speak</button>
            </form>
        """
        resp.content_type = falcon.MEDIA_HTML
