#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import Kmedoids
import KmPurityGini

filename = 'german.txt'
#filename = 'mnist.txt'
#filename = 'test'

data, label = ReadFile.readFile(filename) #读取数据
k = 2 #kmedoids算法的参数k
for i in range(10):
    clusters = Kmedoids.kmedoids(data, k) #进行kmedoids聚类
    print clusters
    purity, giniindex = KmPurityGini.kmPurityGini(label, clusters, k) #计算purity和gini index
    print 'purity: ', purity
    print 'gini index: ', giniindex