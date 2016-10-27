#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import Kmeans
import KmeansPurityGini
import Kmedoids

filename = 'german.txt'
#filename = 'mnist.txt'

data, label = ReadFile.readFile(filename) #读取数据
k = 2 #kmeans算法的参数k
#clusters = Kmeans.kmeans(data, k) #kmeans聚类
#print u'聚类结果：', clusters
#purity, giniindex = KmeansPurityGini.kmeansPurityGini(label, clusters, k)
#print 'purity: ', purity
#print 'gini index: ', giniindex
Kmedoids.kmedoids(data, k)