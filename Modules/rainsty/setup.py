#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   setup.py
@time:   2019-11-03 20:35:27
@description:
"""

import os
import codecs
try:
    from setuptools import setup
except BaseException as e:
    print(e)
    from distutils.core import setup


def read(name):
    file_name = os.path.dirname(__file__)
    result = codecs.open(os.path.join(file_name, name)).read()
    return result


setup(
    name='rainsty',
    version='0.0.2',
    description='This is Residual Mark`s Project.',
    long_description=read('README.md'),
    author='rainsty',
    author_email='1285679912@qq.com',
    url='https://github.com/Rainstyed/rainsty/tree/master/Modules/rainsty',
    license='',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    keywords='Python',
    packages=['rainsty']
)

