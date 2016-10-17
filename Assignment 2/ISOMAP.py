#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import Dijkstra
import Floyd
import MDS

'''
函数功能：
ISOMAP算法，输入样本数据为trainmatdata和testmatdata，参数k为构造连通图时采用的k-NN算法的参数，
type为最短路径算法类型，dimension为所要降的目标维数，函数返回降维结果
数据结构：
输出result是按列组合而成的降维结果矩阵
'''

def isomap(trainmatdata, testmatdata, k, type, dimenson):
    nodemat = hstack((trainmatdata, testmatdata)) #矩阵合并
    nodenum = size(nodemat, 1) #节点数，即数据量
    wgraph = mat(zeros((nodenum, nodenum))) - 1 #节点的连接权重矩阵，初始值都设为-1，表示无穷大
    for num1 in range(nodenum):
        node1 = nodemat[:, num1]
        distances = [] #存储该节点到所有节点的距离（包括自身）
        for num2 in range(nodenum):
            node2 = nodemat[:, num2]
            distances.append(linalg.norm(node1 - node2))
        #取最近的k+1个节点，将距离写入连接权重矩阵（距离最近的为自身）
        indices = argsort(distances)
        for count in range(k + 1):
            wgraph[num1, indices[count]] = distances[indices[count]]
    #将wgraph转化为对称矩阵，即无向图
    for i in range(nodenum):
        for j in range(nodenum):
            if(wgraph[i, j] != -1):
                wgraph[j, i] = wgraph[i, j]

    #计算所有点对之间的最短距离
    if(type == 'dijkstra'):
        distgraph = []
        for i in range(nodenum):
            mindists = Dijkstra.dijkstra(wgraph, i)
            if(size(mindists) == 0): #图不连通
                return []
            distgraph.append(mindists)
        distgraph = mat(distgraph)
    elif(type == 'floyd'):
        distgraph = Floyd.floyd(wgraph)
        if(size(distgraph) == 0): #图不连通
            return []
    else:
        print u'最短距离算法类型错误'
        return []

    #运行MDS算法
    result = MDS.mds(distgraph, dimenson)

    return result