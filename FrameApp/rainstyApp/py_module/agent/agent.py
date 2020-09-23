#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   agent.py
@time:   2020-09-22 15:25:29
@description:
"""


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

    return decorator


def get_action_list():
    return action_list
