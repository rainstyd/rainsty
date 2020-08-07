#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   sklearn_basis.py
@time:   2020-08-06 16:42:29
@description:
"""

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print(reg.coef_)
