#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import Kmeans
import KmeansPurityGini1

filename = 'mnist.txt'
#filename = 'german.txt'

data, label = ReadFile.readFile(filename) #读取数据
k = 10 #kmeans的参数k
clusters = Kmeans.kmeans(data, k) #kmeans聚类
print clusters
#purity, giniindex = KmeansPurityGini1.kmeansPurityGini1(label, clusters) #计算purity和gini index
#print purity, giniindex