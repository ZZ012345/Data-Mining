#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import math

'''
函数功能：

数据结构：

'''

def logisticRegression(data, label):
    T = size(data, axis = 1)  #训练数据量
    D = size(data, axis = 0) #数据维数
    #随机初始化分类器参数向量
    betalist = []
    for i in range(D):
        betalist.append(random.uniform(-1, 1))
    beta = array(betalist)
    print(calculateLoss(data, label, beta, lamda = 1))

def calculateLoss(data, label, beta, lamda):
    T = size(data, axis = 1)
    loss = 0
    for i in range(T):
        instance = data[:, i]
        inslabel = label[i]
        loss = loss + math.log(1 + math.exp(-inslabel * (beta.dot(instance))))
    loss = loss / T + lamda * sum(abs(beta))
    return loss