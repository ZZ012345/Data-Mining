#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：

数据结构：

'''

def kmeansPurityGini(label, clusters, k):
    C = mat(zeros((k, k))) #confusion matrix
    for i in range(size(label)):
        C[label[i], clusters[i]] = C[label[i], clusters[i]] + 1