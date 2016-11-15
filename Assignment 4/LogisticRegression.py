#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
from random import choice
import math
import matplotlib.pyplot as plt

'''
函数功能：

数据结构：

'''

def logisticRegression(traindata, trainlabel, testdata, testlabel, lamda, gamma):
    T = size(traindata, axis=1)  #训练数据量
    D = size(traindata, axis=0) #数据维数
    beta = array([0.01] * D) #初始化分类器参数
    losslist = [calculateLoss(traindata, trainlabel, beta, lamda)[1]] #存储损失函数值
    trainerrorlist = [calculateError(traindata, trainlabel, beta)] #存储训练误差
    testerrorlist = [calculateError(testdata, testlabel, beta)] #存储测试误差
    print('initial loss: ', losslist[0], '; initial train error = ', trainerrorlist[0], '; initial test error = ', testerrorlist[0])
    totaliteration = 10 * T
    step = int(T / 100)
    plotnode = [i for i in range(step, totaliteration, step)] #存储绘图的节点
    #随机梯度下降
    for iterationnum in range(totaliteration): #迭代次数
        if(iterationnum % T == 0):
            indexlist = [i for i in range(T)]
        randindex = choice(indexlist) #随机选择一个数据
        indexlist.remove(randindex)
        instance = traindata[:, randindex]
        inslabel = trainlabel[randindex]
        gradientlist = []
        for j in range(D): #对beta的每一维计算梯度
            temp = math.exp(-inslabel * (beta.dot(instance)))
            if(beta[j] > 0):
                subgradient = 1
            elif(beta[j] < 0):
                subgradient = -1
            else:
                subgradient = 0
            gradientj = temp / (1 + temp) * (-inslabel * instance[j]) + lamda * subgradient
            gradientlist.append(gradientj)
        #更新beta
        beta = beta - gamma * array(gradientlist)
        if(iterationnum in plotnode):
            loss = calculateLoss(traindata, trainlabel, beta, lamda)
            trainerror = calculateError(traindata, trainlabel, beta)
            testerror = calculateError(testdata, testlabel, beta)
            print('迭代次数', iterationnum, ': loss = ', loss, '; train error = ', trainerror, '; test error = ', testerror)
            losslist.append(loss[1])
            trainerrorlist.append(trainerror)
            testerrorlist.append(testerror)
    plotnode.insert(0, 0)
    showFigure(plotnode, losslist, trainerrorlist, testerrorlist, lamda, gamma) #绘图


def calculateLoss(traindata, trainlabel, beta, lamda): #计算损失函数值
    T = size(traindata, axis=1)
    loss = 0
    for i in range(T):
        instance = traindata[:, i]
        inslabel = trainlabel[i]
        loss = loss + math.log(1 + math.exp(-inslabel * (beta.dot(instance))), math.e)
    frontloss = loss / T
    loss = frontloss + lamda * sum(abs(beta))
    return frontloss, loss


def calculateError(data, label, beta): #计算分类错误率
    errornum = 0
    T = size(data, axis=1)
    for i in range(T):
        instance = data[:, i]
        inslabel = label[i]
        betadotx = beta.dot(instance)
        if(inslabel * betadotx <= 0): #分类错误
            errornum = errornum + 1
    return errornum / T

def showFigure(plotnode, losslist, trainerrorlist, testerrorlist, lamda, gamma):
    #绘制损失函数图
    plt.figure(1)
    plt.plot(plotnode, losslist)
    plt.title('Logistic Regression (lambda = ' + str(lamda) + ', learning rate = ' + str(gamma) + ')')
    plt.xlabel('number of iterations')
    plt.ylabel('loss function')
    #绘制错误率图
    plt.figure(2)
    plt.plot(plotnode, trainerrorlist, 'b', label='train error rate')
    plt.plot(plotnode, testerrorlist, 'r', label='test error rate')
    plt.title('Logistic Regression (lambda = ' + str(lamda) + ', learning rate = ' + str(gamma) + ')')
    plt.xlabel('number of iterations')
    plt.ylabel('error rate')
    plt.legend()
    plt.show()