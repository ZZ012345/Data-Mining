#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
快速kmedoids聚类算法，该算法在替换中心点时仅随机选择一个非中心点进行替换，
输入数据data，参数为k，输出用于存储每个数据所属聚类的clusters
注意，该算法中的距离度量采用L1范式
数据结构：
data为mat结构，每一列代表一个数据，clusters为list结构，对应每个数据所属聚类的下标
'''

def fastKmedoids(data, k):
    #计算距离矩阵
    distgraph = computedistgraph(data)
    #随机选择k个中心点
    center = [] #存储中心点的下标
    datanum = size(data, 1)
    for i in range(k):
        num = random.randint(datanum)
        while (num in center):
            num = random.randint(datanum)
        center.append(num)
    other = [i for i in range(datanum)] #存储非中心点的下标
    for i in center:
        other.remove(i)
    clusters = [] #存储每个数据所属聚类的下标
    for i in range(datanum):
        index = center[0]
        mindist = distgraph[i, center[0]]
        for j in range(1, k):
            dist = distgraph[i, center[j]]
            if(dist < mindist):
                index = center[j]
                mindist = dist
        clusters.append(index)

    converge = False
    convnum = 0
    while(not converge):
        # 随机替换5次，取效果最好的
        centerset = []
        costset = []
        newclustersset = []
        for count in range(5):
            #随机选择一个中心点和非中心点
            centernum = center[random.randint(size(center))]
            othernum = other[random.randint(size(other))]
            center_ = [i for i in center]
            center_.append(othernum)
            center_.remove(centernum)
            centerset.append(center_)

            dcosts = []  # 存储每个数据的代价
            newclusters = []  # 存储新的聚类
            #计算新的聚类
            for i in range(datanum):
                index = center_[0]
                mindist = distgraph[i, center_[0]]
                for j in range(1, k):
                    dist = distgraph[i, center_[j]]
                    if (dist < mindist):
                        index = center_[j]
                        mindist = dist
                dcost = distgraph[i, index] - distgraph[i, clusters[i]]
                dcosts.append(dcost)
                newclusters.append(index)
            cost = sum(dcosts) #总的代价
            costset.append(cost)
            newclustersset.append(newclusters)

        # 选择最小的代价
        mincost = min(costset)
        minindex = costset.index(mincost)
        if(mincost < 0):
            #更新聚类
            center = centerset[minindex]
            clusters = newclustersset[minindex]
            convnum = convnum + 1
            print u'迭代次数：', convnum
        else:
            converge = True

    #对聚类结果进行转换，方便后续计算purity和gini index
    clusters = transclusters(clusters, center)

    return clusters


def computedistgraph(data):
    datanum = size(data, 1)
    distgraph = mat(zeros((datanum, datanum)))
    for i in range(datanum):
        for j in range(i + 1, datanum):
            dist = 0.0
            dist = dist + sum(abs(data[:, i] - data[:, j]))
            distgraph[i, j] = dist
            distgraph[j, i] = dist
    return distgraph


def transclusters(clusters, center):
    newclusters = []
    for i in clusters:
        newclusters.append(center.index(i))
    return newclusters