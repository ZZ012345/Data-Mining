#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
MDS算法,输入距离矩阵distgraph和维数dimension，输出降维结果
数据结构：
输出result是按列组合而成的降维结果矩阵
'''

def mds(distgraph, dimension):
    m = size(distgraph, 0) #样本数量
    disti2 = []
    for i in range(0, m, 1):
        temp = 0
        for j in range(0, m, 1):
            temp = temp + distgraph[i, j] * distgraph[i, j]
        temp = temp / m
        disti2.append(temp)
    distj2 = []
    for i in range (0, m, 1):
        temp = 0
        for j in range(0, m, 1):
            temp = temp + distgraph[j, i] * distgraph[j, i]
        temp = temp / m
        distj2.append(temp)
    dist2 = 0
    for i in range(0, m, 1):
        for j in range(0, m, 1):
            dist2 = dist2 + distgraph[i, j] * distgraph[i, j]
    dist2 = dist2 / (m * m)

    B = mat(zeros((m, m))) #初始化降维后样本的内积矩阵
    for i in range(0, m, 1):
        for j in range(0, m, 1):
            B[i, j] = -0.5 * (distgraph[i, j] * distgraph[i, j] - disti2[i] - distj2[j] + dist2)

    #对B做特征值分解
    evals, evcts = linalg.eig(B)
    indices = argsort(evals)  # 计算特征值从小到大排列的下标
    indices = indices[::-1]  # 数组反转
    evals_ = evals[indices[0: dimension]] #取最大的dimension个特征值
    for i in range(0, size(evals_), 1): #将特征值开方
        evals_[i] = sqrt(evals_[i])
    diagmat = diag(evals_) #建立对角矩阵
    evcts_ = evcts[:, indices[0: dimension]] #取最大的dimension个特征值对应的特征向量

    #降维
    result = (evcts_ * diagmat).T
    return result