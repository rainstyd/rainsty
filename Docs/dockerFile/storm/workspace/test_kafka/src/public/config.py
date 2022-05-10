# -*- coding: utf-8 -*-


import os
import configparser
import codecs
import chardet


# =============config.ini======================================================================
ini = configparser.ConfigParser()
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(path, 'config.ini')

with open(file_path, 'rb') as f:
    data = f.read()
    code = chardet.detect(data)

with codecs.open(file_path, 'r', encoding=code['encoding']) as f:
    ini.read_file(f)
# =============config.ini======================================================================

# =============config self=====================================================================
# kafka配置信息
kafka_producer = dict(ini['kafka_producer'])
kafka_consumer = dict(ini['kafka_consumer'])
# =============config self=====================================================================
