#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   api.py
@time:   2019-09-29 09:09
@description:
"""
from flask import request, jsonify
from flask import Blueprint
from src.code import msg

api = Blueprint('main', __name__)


@api.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return jsonify(code=0, msg=msg[0], data=dict(success=True))
