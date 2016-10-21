#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：

数据结构：

'''

def kmeans(data, k):
    datanum = size(data, 1) #数据量
    datadim = size(data, 0) #数据维数
    centernum = []
    for i in range(k): #随机选择k个聚类中心
        num = random.randint(datanum)
        while(num in centernum):
            num = random.randint(datanum)
        centernum.append(num)
    center = [] #存储聚类中心
    for i in centernum:
        center.append(data[:, i])
    clusters = [] #存储各个数据所属的聚类
    for i in range(datanum): #每个数据点所属的聚类都初始化为第一个聚类
        clusters.append(0)

    convergence = False
    while(not convergence):
        newclusters = [] #存储各个数据所属的新的聚类
        #对所有数据点选择所属聚类
        for i in range(datanum):
            dists = []
            for j in range(k):
                #计算距离，采用l1范式
                dist = 0
                for m in range(datadim):
                    dist = dist + float(abs((data[m, i]) - center[j][m]))
                dists.append(dist)
            #选择最近的聚类中心
            newclusters.append(dists.index(min(dists)))
        #判断聚类是否发生变化，即是否收敛
        convergence = True
        for i in range(datanum):
            if(clusters[i] != newclusters[i]):
                convergence = False
                clusters = newclusters
                break
        #未收敛，计算新的聚类中心
        if(not convergence):
            clusterset = [] #存储每个聚类中的数据的下标
            for i in range(k):
                clusterset.append([])
            for i in range(datanum):
                clusterset[newclusters[i]].append(i)
            for i in range(k):
                datasum = mat(zeros((datadim, 1)))
                for j in clusterset[i]:
                    datasum = datasum + data[:, j]
                datasum = datasum / size(clusterset[i])
                center[i] = datasum

    return clusters