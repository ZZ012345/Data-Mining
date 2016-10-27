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
        costs = [] #存储用a替换b的代价
        newclusters = [] #存储每次替换后对应的新的聚类
        for a in other:
            for b in center:
                #用a替换b
                center_ = [i for i in center]
                center_.remove(b)
                center_.append(a)
                other_ = [i for i in other]
                other_.remove(a)
                other_.append(b)
                dcosts = [] #存储每个数据的代价
                newcluster = [] #存储新的聚类
                #对每个数据计算新的所属聚类
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
                    newcluster.append(index)
                #计算并存储总的代价
                costs.append(sum(dcosts))
                #存储新的聚类
                newclusters.append(newcluster)
        #取最小代价
        mincost = min(costs)
        indice = costs.index(mincost)
        if(mincost < 0):
            #更新聚类
            clusters = newclusters[indice]
            #更新center和other
            b = center[indice % k]
            a = other[(indice - indice % k) / k]
            center.remove(b)
            center.append(a)
            other.remove(a)
            other.append(b)
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