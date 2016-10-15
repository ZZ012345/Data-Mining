#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import Dijkstra

'''
函数功能：

数据结构：

'''

def ISOMAP(trainmatdata, testmatdata, k):
    nodemat = hstack((trainmatdata, testmatdata)) #矩阵合并
    nodenum = size(nodemat, 1) #节点数，即数据量
    wgraph = mat(zeros((nodenum, nodenum))) - 1 #节点的连接权重矩阵，初始值都设为-1，表示无穷大
    for num1 in range(0, nodenum, 1):
        node1 = nodemat[:, num1]
        distances = [] #存储该节点到所有节点的距离（包括自身）
        for num2 in range(0, nodenum, 1):
            node2 = nodemat[:, num2]
            distances.append(linalg.norm(node1 - node2))
        #取最近的k+1个节点，将距离写入连接权重矩阵（距离最近的为自身）
        indices = argsort(distances)
        for count in range(0, k + 1, 1):
            wgraph[num1, indices[count]] = distances[indices[count]]
    mindists = Dijkstra.dijkstra(wgraph, 0)
    print mindists