#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
from random import choice

'''
函数功能：

数据结构：

'''

def ridgeRegression(traindata, trainlabel, testdata, testlabel, lamda, gamma):
    T = size(traindata, axis = 1)  #训练数据量
    D = size(traindata, axis = 0) #数据维数
    beta = ones(D) #初始化分类器参数
    print('initial loss: ', calculateLoss(traindata, trainlabel, beta, lamda), '; initial train error = ',\
          calculateError(traindata, trainlabel, beta), '; initial test error = ', calculateError(testdata, testlabel, beta))
    step = int(T / 100)
    plotnode = [] #存储绘图的节点
    for i in range(step, T, step):
        plotnode.append(i)
    #随机梯度下降
    for iterationnum in range(T): #迭代次数
        if (iterationnum % T == 0):
            indexlist = [i for i in range(T)]
        randindex = choice(indexlist) #随机选择一个数据
        indexlist.remove(randindex)
        instance = traindata[:, randindex]
        inslabel = trainlabel[randindex]
        gradientlist = []
        for j in range(D): #对beta的每一维计算梯度
            gradientj = 2 * (inslabel - beta.dot(instance)) * (-instance[j]) + 2 * lamda * beta[j]
            gradientlist.append(gradientj)
        #更新beta
        beta = beta - gamma * array(gradientlist)
        if(iterationnum in plotnode):
            print('迭代次数', iterationnum, ': loss = ', calculateLoss(traindata, trainlabel, beta, lamda), \
                  '; train error = ', calculateError(traindata, trainlabel, beta), '; test error = ', calculateError(testdata, testlabel, beta))


def calculateLoss(traindata, trainlabel, beta, lamda): #计算损失函数值
    T = size(traindata, axis = 1)
    loss = 0
    for i in range(T):
        instance = traindata[:, i]
        inslabel = trainlabel[i]
        loss = loss + (inslabel - beta.dot(instance)) ** 2
    frontloss = loss / T
    loss = frontloss + lamda * sum(beta * beta)
    return frontloss, loss


def calculateError(data, label, beta): #计算分类错误率
    errornum = 0
    T = size(data, axis = 1)
    for i in range(T):
        instance = data[:, i]
        inslabel = label[i]
        betadotx = beta.dot(instance)
        if(inslabel * betadotx <= 0): #分类错误
            errornum = errornum + 1
    return errornum / T