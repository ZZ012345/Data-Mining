#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
最短路径算法，计算连接权重矩阵wgraph中各个节点之间的最短距离
数据结构：
返回的用于存放最短距离的distgraph为矩阵结构
'''

def floyd(wgraph):
    n = size(wgraph, 0)
    distgraph = wgraph #用于存放最终结果，初始化为wgraph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(wgraph[i, k] != -1 and wgraph[k, j] != -1):
                    sum = wgraph[i, k] + wgraph[k, j]
                    if(wgraph[i, j] == -1):
                        wgraph[i, j] = sum
                    else:
                        wgraph[i, j] = min(wgraph[i, j], sum)
    #判断图是否连通
    for i in range(n):
        for j in range(n):
            if(distgraph[i, j] == -1):
                print u'该图不连通'
                return []

    return distgraph