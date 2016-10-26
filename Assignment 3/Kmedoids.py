#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
kmedoids聚类算法，输入数据data，参数为k，输出用于存储每个数据所属聚类的clusters
注意，该算法中的距离度量采用L1范式
数据结构：
data为mat结构，每一列代表一个数据，clusters为list结构，对应每个数据所属聚类的下标
'''

def kmedoids(data, k):
    #计算距离矩阵
    distgraph = computedistgraph(data)
    #随机选择k个中心点


def computedistgraph(data):
    datanum = size(data, 1)
    datadim = size(data, 0)
    distgraph = mat(zeros((datanum, datanum)))
    for i in range(datanum):
        for j in range(i + 1, datanum):
            dist = 0.0
            temp = data[i] - data[j]
            for k in range(datadim):
                dist = dist + abs(temp[k])
            distgraph[i, j] = dist
            distgraph[j, i] = dist
    return distgraph