#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   __init__.py
@time:   2020-09-22 15:24:29
@description:
"""

from .agent import action
from .agent import get_action_list

# # !/usr/bin/env python
# # encoding: utf-8
# # 如果觉得不错，可以推荐给你的朋友！http://tool.lu/pyc
# import sys
# import importlib
# import py_module.action as py_module
# import os
# import re
# import inspect
# from imp import reload
#
# action_dict = {}
# action_class_list = {}
# actions = []
# IsDebug = False
# config = {}
# isInteract = False
# sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'packages'))
#
#
# def getconfig(section, name, default=None):
#     if section in config and name in config[section]:
#         return config[section][name]
#
#
# def get_actionlist():
#     '''\xe6\x9f\xa5\xe6\x89\xbe\xe5\x8a\x9f\xe8\x83\xbd\xe5\x88\x97\xe8\xa1\xa8'''
#     folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'action')
#     d = os.listdir(folder)
#     funcs = (lambda .0: for o in .0:
#     if not o[-3:] == '.py':
#         if
#     o[-4:] == '.pyc':
#
#
# continue
# [][o.split('.')[0]])(d)
# funcs = list(set(funcs))
# for o in funcs:
#     importlib.import_module('py_module.action.' + o)
#
# return actions
#
#
# def do_action(func_action, req, ans, intf):
#     '''\xe6\x89\xa7\xe8\xa1\x8c\xe4\xbb\xbb\xe5\x8a\xa1'''
#     global isInteract
#     if func_action in action_dict:
#         (func, cls, inst) = action_dict[func_action]
#         if IsDebug:
#             module = inspect.getmodule(func)
#             reload(module)
#             (func, cls, inst) = action_dict[func_action]
#         if not req['python'] == 'zmkm' and isInteract:
#             isInteract = True
#             import threading
#
#             def run():
#                 import code
#
#                 getfunc = lambda x: action_dict[x][0]
#                 code.interact(local=locals())
#
#             p = threading.Thread(target=run, daemon=True)
#             p.start()
#         if cls is None:
#             return func(req, ans, intf)
#         if None is None:
#             inst = cls()
#             action_dict[func_action] = (func, cls, inst)
#         return func(inst, req, ans, intf)
#
#
# def action(func_action, name, version, file='', **options):
#     '''
#     \xe8\xbe\x85\xe5\x8a\xa9\xe6\x96\xb9\xe6\xb3\x95\xef\xbc\x8c\xe9\x80\x9a\xe8\xbf\x87\xe6\xad\xa4\xe6\x96\xb9\xe6\xb3\x95\xe8\x8e\xb7\xe5\x8f\x96Action\xe5\x88\x97\xe8\xa1\xa8\xe5\x92\x8cAction\xe5\xad\x97\xe5\x85\xb8
#     '''
#
#     def decorator(f):
#         action_dict[func_action] = (f, None, None)
#         sfile = ''
#         if file:
#             sfile = ' - ' + os.path.basename(file)
#         if IsDebug:
#             actions.append((func_action, '[Debug]' + str(name) + sfile, version))
#         else:
#             actions.append((func_action, str(name) + sfile, version))
#         return f
#
#     return decorator
#
#
# def register_actionclass(cls):
#     for func_action in action_dict:
#         (f, m_class, m_inst) = action_dict[func_action]
#         if hasattr(cls, f.__name__) and getattr(cls, f.__name__) == f:
#             action_dict[func_action] = (f, cls, None)
#
#
# def do_init():
#     print(
#         '\xe6\xac\xa2\xe8\xbf\x8e\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad\xe7\x84\xafPython\xe7\x89\x88\xe4\xb8\xad\xe9\x97\xb4\xe4\xbb\xb6(' + py_module.agent.__version__ + ').\nPython ',
#         sys.version)
#     get_actionlist()
#
#
# import sys
# import importlib
# import py_module.action as py_module
# import os
# import re
# import inspect
# from imp import reload
#
# action_dict = {}
# action_class_list = {}
# actions = []
# IsDebug = False
# config = {}
# isInteract = False
# sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'packages'))
#
#
# def getconfig(section, name, default=None):
#     if section in config and name in config[section]:
#         return config[section][name]
#
#
# def get_actionlist():
#     '''\xe6\x9f\xa5\xe6\x89\xbe\xe5\x8a\x9f\xe8\x83\xbd\xe5\x88\x97\xe8\xa1\xa8'''
#     folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'action')
#     d = os.listdir(folder)
#     funcs = (lambda .0: for o in .0:
#     if not o[-3:] == '.py':
#         if
#     o[-4:] == '.pyc':
#
#
# continue
# [][o.split('.')[0]])(d)
# funcs = list(set(funcs))
# for o in funcs:
#     importlib.import_module('py_module.action.' + o)
#
# return actions
#
#
# def do_action(func_action, req, ans, intf):
#     '''\xe6\x89\xa7\xe8\xa1\x8c\xe4\xbb\xbb\xe5\x8a\xa1'''
#     global isInteract
#     if func_action in action_dict:
#         (func, cls, inst) = action_dict[func_action]
#         if IsDebug:
#             module = inspect.getmodule(func)
#             reload(module)
#             (func, cls, inst) = action_dict[func_action]
#         if not req['python'] == 'zmkm' and isInteract:
#             isInteract = True
#             import threading
#
#             def run():
#                 import code
#
#                 getfunc = lambda x: action_dict[x][0]
#                 code.interact(local=locals())
#
#             p = threading.Thread(target=run, daemon=True)
#             p.start()
#         if cls is None:
#             return func(req, ans, intf)
#         if None is None:
#             inst = cls()
#             action_dict[func_action] = (func, cls, inst)
#         return func(inst, req, ans, intf)
#
#
# def action(func_action, name, version, file='', **options):
#     '''
#     \xe8\xbe\x85\xe5\x8a\xa9\xe6\x96\xb9\xe6\xb3\x95\xef\xbc\x8c\xe9\x80\x9a\xe8\xbf\x87\xe6\xad\xa4\xe6\x96\xb9\xe6\xb3\x95\xe8\x8e\xb7\xe5\x8f\x96Action\xe5\x88\x97\xe8\xa1\xa8\xe5\x92\x8cAction\xe5\xad\x97\xe5\x85\xb8
#     '''
#
#     def decorator(f):
#         action_dict[func_action] = (f, None, None)
#         sfile = ''
#         if file:
#             sfile = ' - ' + os.path.basename(file)
#         if IsDebug:
#             actions.append((func_action, '[Debug]' + str(name) + sfile, version))
#         else:
#             actions.append((func_action, str(name) + sfile, version))
#         return f
#
#     return decorator
#
#
# def register_actionclass(cls):
#     for func_action in action_dict:
#         (f, m_class, m_inst) = action_dict[func_action]
#         if hasattr(cls, f.__name__) and getattr(cls, f.__name__) == f:
#             action_dict[func_action] = (f, cls, None)
#
#
# def do_init():
#     print(
#         '\xe6\xac\xa2\xe8\xbf\x8e\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad\xe7\x84\xafPython\xe7\x89\x88\xe4\xb8\xad\xe9\x97\xb4\xe4\xbb\xb6(' + py_module.agent.__version__ + ').\nPython ',
#         sys.version)
#     get_actionlist()
#
