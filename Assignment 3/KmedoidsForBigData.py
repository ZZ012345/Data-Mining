#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
适用于大数据的kmedoids聚类算法，
该算法在替换中心点时遍历所有选择并在其中选择最佳替换，并且不会存储距离矩阵以防内存不够，
输入数据data，参数为k，输出用于存储每个数据所属聚类的clusters
注意，该算法中的距离度量采用L1范式
数据结构：
data为mat结构，每一列代表一个数据，clusters为list结构，对应每个数据所属聚类的下标
'''

def kmedoidsForBigData(data, k):
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
        mindist = sum(abs(data[:, i] - data[:, center[0]]))
        for j in range(1, k):
            dist = sum(abs(data[:, i] - data[:, center[j]]))
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
                dcosts = [] #存储每个数据的代价
                newcluster = [] #存储新的聚类
                #对每个数据计算新的所属聚类
                for i in range(datanum):
                    index = center_[0]
                    mindist = sum(abs(data[:, i] - data[:, center_[0]]))
                    for j in range(1, k):
                        dist = sum(abs(data[:, i] - data[:, center_[j]]))
                        if (dist < mindist):
                            index = center_[j]
                            mindist = dist
                    dcost = sum(abs(data[:, i] - data[:, index])) - sum(abs(data[:, i] - data[:, clusters[i]]))
                    dcosts.append(dcost)
                    newcluster.append(index)
                #计算并存储总的代价
                costs.append(sum(dcosts))
                #存储新的聚类
                newclusters.append(newcluster)
        #取最小代价
        mincost = min(costs)
        minindex = costs.index(mincost)
        if(mincost < 0):
            #更新聚类
            clusters = newclusters[minindex]
            #更新center和other
            b = center[minindex % k]
            a = other[(minindex - minindex % k) / k]
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


def transclusters(clusters, center):
    newclusters = []
    for i in clusters:
        newclusters.append(center.index(i))
    return newclusters