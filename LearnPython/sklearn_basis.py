#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   sklearn_basis.py
@time:   2020-08-06 16:42:29
@description:
"""

from pyrainsty import connect
from sklearn import linear_model
from sklearn.cluster import KMeans
from random import randint


# reg = linear_model.LinearRegression()
# reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
# print(reg.coef_)

label = []
for i in range(1000):
     label.append('label{}'.format(i))

user = []
for i in range(1000):
     u = []
     for j in range(len(label)):
          s = randint(0, 10)
          if s == 1:
               u.append(1)
          else:
               u.append(0)
     user.append(u)

clf = KMeans(n_clusters=4)
y_pred = clf.fit_predict(user)

# 输出完整的kmeans函数，包括很多省略参数
# print(clf)
# 输出聚类预测结果，20行数据，每个y_pred对应x一行或一个球员，聚成三类，类标为0,1,2
# print(y_pred)

l_0 = {}
l_1 = {}
l_2 = {}
l_3 = {}

for i in range(len(y_pred)):
     d = y_pred[i]
     if d == 0:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_0[label[j]] = l_0.get(label[j], 0) + 1

     if d == 1:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_1[label[j]] = l_1.get(label[j], 0) + 1

     if d == 2:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_2[label[j]] = l_2.get(label[j], 0) + 1

     if d == 3:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_3[label[j]] = l_3.get(label[j], 0) + 1

l_0 = sorted(l_0.items(), key=lambda x: x[1], reverse=True)
l_1 = sorted(l_1.items(), key=lambda x: x[1], reverse=True)
l_2 = sorted(l_2.items(), key=lambda x: x[1], reverse=True)
l_3 = sorted(l_3.items(), key=lambda x: x[1], reverse=True)

# l_1 = sorted(l_1, reverse=True)
# l_2 = sorted(l_2, reverse=True)
# l_3 = sorted(l_3, reverse=True)

print(l_0[:10])
print(l_1[:10])
print(l_2[:10])
print(l_3[:10])

# print(l_0[:10])
# print(l_1[:10])
# print(l_2[:10])
# print(l_3[:10])

l_0 = {}
l_1 = {}
l_2 = {}
l_3 = {}

for i in range(len(y_pred)):
     d = y_pred[i]
     if d == 0:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_0[label[j]] = l_0.get(label[j], 0) + 1

     if d == 1:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_1[label[j]] = l_1.get(label[j], 0) + 1

     if d == 2:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_2[label[j]] = l_2.get(label[j], 0) + 1

     if d == 3:
          for j in range(len(user[i])):
               if user[i][j] == 1:
                    l_3[label[j]] = l_3.get(label[j], 0) + 1

l_0 = sorted(l_0.items(), key=lambda x: x[1], reverse=True)
l_1 = sorted(l_1.items(), key=lambda x: x[1], reverse=True)
l_2 = sorted(l_2.items(), key=lambda x: x[1], reverse=True)
l_3 = sorted(l_3.items(), key=lambda x: x[1], reverse=True)

# l_1 = sorted(l_1, reverse=True)
# l_2 = sorted(l_2, reverse=True)
# l_3 = sorted(l_3, reverse=True)

print(l_0[:10])
print(l_1[:10])
print(l_2[:10])
print(l_3[:10])

# print(l_0[:10])
# print(l_1[:10])
# print(l_2[:10])
# print(l_3[:10])
