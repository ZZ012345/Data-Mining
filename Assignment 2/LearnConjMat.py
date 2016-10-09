#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
计算投影矩阵，返回学习到的特征值和特征向量
数据结构：
输入matdata是测试数据集按列组合而成的矩阵，返回的evals是特征值从大到小排列而成的数组，
返回的evcts是特征值对应的特征向量按列组成的矩阵
'''

def learnConjMat(matdata):
    #数据标准化
    meandata = mean(matdata, axis = 1) #按行求均值，即每个特征的均值
    matdata = matdata - meandata
    #计算协方差矩阵
    covmat = matdata * matdata.T / size(matdata, 1)
    #计算特征值和特征向量
    evals, evcts = linalg.eig(covmat)
    #将特征值按从大到小进行排序
    indices = argsort(evals) #计算特征值从小到大排列的下标
    indices = indices[::-1] #数组反转
    evals = evals[indices]
    evcts = evcts[:, indices]
    return evals, evcts