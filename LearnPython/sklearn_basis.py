#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   sklearn_basis.py
@time:   2020-08-06 16:42:29
@description:
"""

from sklearn import linear_model
from sklearn.cluster import KMeans


reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print(reg.coef_)


x = [[0.0888, 0.5885],
     [0.1399, 0.8291],
     [0.0747, 0.4974],
     [0.0983, 0.5772],
     [0.1276, 0.5703],
     [0.1671, 0.5835],
     [0.1906, 0.5276],
     [0.1061, 0.5523],
     [0.2446, 0.4007],
     [0.1670, 0.4770],
     [0.2485, 0.4313],
     [0.1227, 0.4909],
     [0.1240, 0.5668],
     [0.1461, 0.5113],
     [0.2315, 0.3788],
     [0.0494, 0.5590],
     [0.1107, 0.4799],
     [0.2521, 0.5735],
     [0.1007, 0.6318],
     [0.1067, 0.4326],
     [0.1956, 0.4280]
]

print(x)
clf = KMeans(n_clusters=3)
y_pred = clf.fit_predict(x)

# 输出完整的kmeans函数，包括很多省略参数
print(clf)
# 输出聚类预测结果，20行数据，每个y_pred对应x一行或一个球员，聚成三类，类标为0,1,2
print(y_pred)
