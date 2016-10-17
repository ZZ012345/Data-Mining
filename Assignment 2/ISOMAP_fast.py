#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import Dijkstra_fast
import MDS

'''
函数功能：
ISOMAP算法，输入样本数据为trainmatdata和testmatdata，参数k为构造连通图时采用的k-NN算法的参数，
dimension为所要降的目标维数，函数返回降维结果
数据结构：
输出result是按列组合而成的降维结果矩阵
'''

def isomap_fast(trainmatdata, testmatdata, k, dimenson):
    nodemat = hstack((trainmatdata, testmatdata)) #矩阵合并
    nodenum = size(nodemat, 1) #节点数，即数据量
    #构造用于存储距离信息的字典
    wgraph = {i:{} for i in range(nodenum)}
    for i in range(nodenum):
        node1 = nodemat[:, i]
        distances = []
        for j in range(nodenum):
            node2 = nodemat[:, j]
            distances.append(linalg.norm(node1 - node2))
        indices = argsort(distances)
        for count in range(1, k + 1, 1):
            wgraph[i][indices[count]] = distances[indices[count]]
            wgraph[indices[count]][i] = distances[indices[count]]

    #计算所有点对之间的最短距离
    distgraph = []
    mindists = Dijkstra_fast.dijkstra_fast(wgraph, 0)
    for i in range(1, nodenum):
        if(mindists[i] == 0):
            print u'该图不连通'
            return []
    distgraph.append(mindists)
    for i in range(1, nodenum):
        mindists = Dijkstra_fast.dijkstra_fast(wgraph, i)
        distgraph.append(mindists)
        print i
    distgraph = mat(distgraph)

    #运行MDS算法
    result = MDS.mds(distgraph, dimenson)

    return result