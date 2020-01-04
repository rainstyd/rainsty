#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   test.py
@time:   2020-01-04 18:36:57
@description:
"""

import os
from pyspark.sql import SparkSession

os.environ['JAVA_HOME'] = '/root/jdk'
os.environ['PYTHON_HOME'] = "/root/python"
os.environ['PYSPARK_PYTHON'] = "/usr/bin/python"
os.environ['SPARK_HOME'] = '/root/spark'
os.environ['SPARK_MASTER_IP'] = 'rainsty'


def create_spark_context():

    sc = SparkSession.builder \
        .appName("TestSparkSession") \
        .master("spark://rainsty:7077") \
        .config('spark.executor.num', '1')\
        .config('spark.executor.memory', '512m')\
        .config("spark.executor.cores", '1')\
        .config('spark.cores.max', '1')\
        .config('spark.driver.memory', '512m') \
        .getOrCreate()

    return sc


logFile = "/root/spark/README.md"
spark = create_spark_context()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
