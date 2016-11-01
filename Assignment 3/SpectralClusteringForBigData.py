#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

import Kmedoids
import FastKmedoidsForBigData

'''
函数功能：
适用于大数据的谱聚类算法，该算法并不会存储距离矩阵以防内存不够，
输入数据为data，构建邻接矩阵时所用的kNN算法的参数为n，kmedoids聚类时参数为k，
kmedoids算法类型为kmedoidtype，输出聚类结果clusters
数据结构：
data为mat结构，每一列代表一个数据，clusters为list结构，对应每个数据所属聚类的下标
'''

def spectralClusteringForBigData(data, n, k, kmedoidstype):
    datanum = size(data, 1)

    #构建邻接矩阵
    adjgraph = mat(zeros([datanum, datanum]))
    for i in range(datanum):
        #计算第i个数据到所有其他数据的距离
        diff = tile(data[:, i], (1, datanum)) - data
        squareddiff = square(diff)
        squareddist = sum(squareddiff, axis = 0) #按列求和
        indices = argsort(squareddist)
        for count in range(1, n + 1):
            adjgraph[i, indices[0, count]] = 1
            adjgraph[indices[0, count], i] = 1

    #构建对角矩阵
    diaglist = []
    for i in range(datanum):
        diaglist.append(sum(adjgraph[:, i]))
    diagmat = diag(diaglist)

    L = diagmat - adjgraph #拉普拉斯矩阵
    M = linalg.inv(diagmat) * L
    evals, evcts = linalg.eig(M) #求特征值和特征向量
    indices = argsort(evals) #计算特征值从小到大排列的下标
    evals = evals[indices]
    evcts = evcts[:, indices]
    minevcts = evcts[:, 1:(k+1)] #取最小的k个特征向量（不包括最小的）
    redata = minevcts.T #降维
    print u'降维结束，开始kmedoids聚类...'

    #kmedoids聚类
    if(kmedoidstype == 'normal'):
        clusters = Kmedoids.kmedoids(redata, k)
    elif(kmedoidstype == 'fast'):
        clusters = FastKmedoidsForBigData.fastKmedoidsForBigData(redata, k)

    return clusters