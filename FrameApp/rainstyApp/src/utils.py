#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   utils.py
@time:   2019-12-30 15:33:29
@description:
"""

import os
import errno
import logging
import datetime


class MidnightRotatingFileHandler(logging.FileHandler):
    def __init__(self, filename):
        self._filename = filename
        self._rotate_at = self._next_rotate_datetime()
        super(MidnightRotatingFileHandler, self).__init__(filename, mode='a')

    @staticmethod
    def _next_rotate_datetime():
        now = datetime.datetime.now()
        return now.replace(hour=0, minute=0, second=0) + datetime.timedelta(days=1)

    def _open(self):
        now = datetime.datetime.now()
        log_today = "%s.%s" % (self._filename, now.strftime('%Y-%m-%d'))
        try:
            fd = os.open(log_today, os.O_CREAT | os.O_EXCL)
            os.close(fd)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.baseFilename = log_today
        return super(MidnightRotatingFileHandler, self)._open()

    def emit(self, record):
        now = datetime.datetime.now()
        if now > self._rotate_at:
            self._rotate_at = self._next_rotate_datetime()
            self.close()
        super(MidnightRotatingFileHandler, self).emit(record)


class Logger(object):
    """
    example:
        from pyrainsty import logger
        logger = logger.Logger(base_path, log_dir_name, log_file_name)
        logger = logger.get_logger()
    """

    def __init__(self, base_path, log_dir_name, log_file_name, log_format=None):
        """
        :desc logger
        :param base_path:
        :param log_dir_name:
        :param log_file_name:
        :param log_format:
        """
        self.__base_path = base_path
        self.__log_dir_name = log_dir_name
        self.__log_file_name = log_file_name
        self.__logger = logging.getLogger()
        self.__log_format = log_format

    def get_logger(self):
        log_format = '[%(asctime)s] %(levelname)s %(pathname)s:%(lineno)d %(message)s'

        self.__logger.setLevel(logging.INFO)
        self.__log_format = self.__log_format if self.__log_format else log_format

        log_dir_path = os.path.join(self.__base_path, self.__log_dir_name)
        if not os.path.exists(log_dir_path):
            os.makedirs(log_dir_path)

        log_file_folder = os.path.join(log_dir_path, self.__log_file_name)
        file_log_handler = MidnightRotatingFileHandler(log_file_folder)

        formatter = logging.Formatter(self.__log_format)
        file_log_handler.setFormatter(formatter)
        self.__logger.addHandler(file_log_handler)
        return self.__logger
