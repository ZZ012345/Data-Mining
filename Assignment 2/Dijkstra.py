#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
单源最短路径算法，计算连接权重矩阵wgraph中第nodenum个节点到其他所有节点之间的最短距离
数据结构：
返回的用于存放最短距离的mindists为list结构
'''

def dijkstra(wgraph, nodenum):
    amount = size(wgraph, 0)
    #初始化用于存放最短距离的list
    mindists = []
    for i in range(0, amount, 1):
        mindists.append(-1)
    mindists[nodenum] = 0 #到自身最短距离为0
    u = [] #用于存放已经求出最短距离的节点
    u.append(nodenum)
    v = [] #用于存放还未求出最短距离的节点
    for i in range(0, amount, 1):
        if i != nodenum:
            v.append(i)
    #添加最近的节点
    indices = argsort(wgraph[nodenum, :])
    count = 1
    while(wgraph[nodenum, indices[0, -count]] != -1 and wgraph[nodenum, indices[0, -count]] != 0):
        mindists[indices[0, -count]] = wgraph[nodenum, indices[0, -count]]
        count = count + 1
    lastnode = indices[0, -count + 1]#上一个添加进u的节点
    u.append(lastnode)
    v.remove(lastnode)

    while(size(v) != 0):
        for i in range(0, amount, 1):
            if(wgraph[lastnode, i] != -1 and wgraph[lastnode, i] != 0 and i not in u): #取出与上一个添加的节点相连的节点
                if(mindists[i] != -1 and mindists[i] != 0): #之前图已经连接到该节点
                    if(wgraph[lastnode, i] + mindists[lastnode] < mindists[i]):
                        mindists[i] = wgraph[lastnode, i] + mindists[lastnode] #更新距离
                else: #之前图未连接到该节点
                    mindists[i] = wgraph[lastnode, i] + mindists[lastnode]
        #对于不在u中的节点，选择最近的一个添加到u中
        candnode = [] #候选点集合
        for i in range(0, amount, 1):
            if(i not in u and mindists[i] != -1):
                candnode.append(i)
        if(size(candnode) == 0):
            print u'该图不连通'
            return []
        addnode = candnode[0]
        for node in candnode:
            if(mindists[node] < mindists[addnode]):
                addnode = node
        #添加节点
        u.append(addnode)
        v.remove(addnode)
        lastnode = addnode

    return mindists