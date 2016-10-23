#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
根据kmeans聚类结果计算purity和gini index，输入的是每个数据的标签和聚类以及参数k，输出purity和gini index
数据结构：
label和clusters是由int构成的list结构，它们之间一一对应，purity和gini index为float型
'''

def kmeansPurityGini(label, clusters, k):
    C = mat(zeros((k, k))) #confusion matrix
    for i in range(size(label)):
        C[label[i], clusters[i]] = C[label[i], clusters[i]] + 1

    #计算purity
    p = []
    m = []
    for i in range(k):
        max = 0
        sum = 0
        for j in range(k):
            max = (C[j, i] if C[j, i] > max else max)
            sum = sum + C[j, i]
        p.append(max)
        m.append(sum)
    sump = 0
    summ = 0
    for i in range(k):
        sump = sump + p[i]
        summ = summ + m[i]
    purity = sump /summ

    #计算gini index
    g = []
    for i in range(k):
        gi = 1
        for j in range(k):
            gi = gi - square(C[j, i] / m[i])
        g.append(gi)
    sumgm = 0
    for i in range(k):
        sumgm = sumgm + g[i] * m[i]
    giniindex = sumgm / summ

    return purity, giniindex