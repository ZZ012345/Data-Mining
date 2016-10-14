#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：

数据结构：

'''

def ISOMAP(trainmatdata, testmatdata, k):
    nodedata = hstack((trainmatdata, testmatdata)) #矩阵合并
    nodenum = size(nodedata, 1) #节点数，即数据量
    wgraph = zeros((nodenum, nodenum)) - 1 #节点的连接权重矩阵，初始值都设为-1
    for num in range(0, nodenum, 1): #对角线设为0
        wgraph[num][num] = 0
