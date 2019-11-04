#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   setup.py
@time:   2019-11-03 20:35:27
@description:
"""

import os
try:
    from setuptools import setup
except BaseException as e:
    print(e)
    from distutils.core import setup


with open("README.md", "r") as fh:
        long_description = fh.read()


setup(
    name='rainsty',
    version='0.0.3',
    author='rainsty',
    author_email='1285679912@qq.com',
    description='This is Residual Mark`s Project.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Rainstyed/rainsty/tree/master/Modules/rainsty',
    packages=['src'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)

