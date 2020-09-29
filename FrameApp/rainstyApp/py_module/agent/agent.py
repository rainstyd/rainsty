#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   agent.py
@time:   2020-09-22 15:25:29
@description:
"""

import functools


action_list = []
action_dict = {}


def action(_action, _name, _method):

    def decorator(_func):
        global action_dict
        action_dict['action'] = _action
        action_dict['name'] = _name
        action_dict['class'] = _func
        action_dict['method'] = _method
        action_list.append(action_dict)
        action_dict = {}

        @functools.wraps(_func)
        def w(*args, **kwargs):
            print('call %s(): the param is %s,%s,%s.' % (_func.__name__, _action, _name, _method))
            return _func(*args, **kwargs)

        return w
    return decorator


def get_action_list():
    return action_list
