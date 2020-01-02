#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   config.py
@time:   2019-12-30 13:36:29
@description:
"""

import os
from pyrainsty import logger
from configparser import ConfigParser


class AppConfig(object):

    base_path = os.path.dirname(os.path.dirname(__file__))
    sqlite_db_path = r'sqlite:///{}'.format(os.path.join(base_path, 'sqlite.db'))

    log_dir_name = 'logs'
    log_file_name = 'falconApp.log'

    config_file = os.path.join(base_path, 'version.ini')
    conf = ConfigParser()
    conf.read(config_file)
    version = dict(conf.items('config')).get('version', 'v0.0.1')

    route_path = '/api/{}'.format(version)

    logger = logger.Logger(base_path, log_dir_name, log_file_name)
    logger = logger.get_logger()

    SECRET_KEY = 'fds545jjl665jni222nbi779bla110jnl335'
