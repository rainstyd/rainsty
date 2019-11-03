#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   setup.py
@time:   2019-11-03 20:35:27
@description:
"""
import os
import codecs
from distutils.core import setup
from setuptools import find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='rainsty',
    version='0.0.1',
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
    keywords='',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)

