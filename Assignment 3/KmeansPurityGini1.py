#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：

数据结构：

'''

def kmeansPurityGini1(label, clusters):
    C = mat(zeros((2, 2))) #confusion matrix
    for i in range(size(clusters)):
        if(label[i] == 1):
            if(clusters[i] == 1):
                C[0, 0] = C[0, 0] + 1
            else:
                C[0, 1] = C[0, 1] + 1
        else:
            if(clusters[i] == 1):
                C[1, 1] = C[1, 1] + 1
            else:
                C[1, 0] = C[1, 0] + 1

    #计算purity
    p1 = (C[0, 0] if C[0, 0] > C[1, 0] else C[1, 0])
    p2 = (C[0, 1] if C[0, 1] > C[1, 1] else C[1, 1])
    m1 = C[0, 0] + C[1, 0]
    m2 = C[0, 1] + C[1, 1]
    purity = (p1 + p2) / (m1 + m2)

    #计算Gini index
    g1 = 1 - square(C[0, 0] / m1) - square(C[1, 0] / m1)
    g2 = 1 - square(C[0, 1] / m2) - square(C[1, 1] / m2)
    giniindex = (g1 * m1 + g2 * m2) / (m1 + m2)

    return purity, giniindex