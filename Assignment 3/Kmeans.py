#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：

数据结构：

'''

def kmeans(data, k):
    datanum = size(data, 1) #数据量
    centernum = []
    for i in range(k): #随机选择k个聚类中心
        num = random.randint(datanum)
        while(num in centernum):
            num = random.randint(datanum)
        centernum.append(num)
    center = [] #存储聚类中心
    for i in centernum:
        center.append(data[:, i])
    clusters = [[None]] * k #存储各个聚类中的数据下标
    for i in range(datanum): #每个点所属的聚类都初始化为第一个聚类
        clusters[0].append(i)

    convergence = False
    while(not convergence):