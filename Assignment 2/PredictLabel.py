#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：

数据结构：

'''

def predictLabel(finaltraindata, trainlabel, finaltestdata, testlabel):
    traindatanum = size(finaltraindata, 1) #训练数据量
    trainlabelnum = len(trainlabel) #训练标签量
    testdatanum = size(finaltestdata, 1) #测试数据量
    testlabelnum = len(testlabel) #测试标签量
    if traindatanum != trainlabelnum or testdatanum != testlabelnum:
        print u'输入数据数量与标签数量不相等'
        return

    testnum = 0
    isright = [] #存储测试数据标签的正确性，1表示正确，0表示错误
    while testnum < testdatanum:
        testdata = finaltestdata[:, testnum] #取测试数据
        distances = [] #用于存储测试数据与训练数据之间的距离
        trainnum = 0
        while trainnum < traindatanum:
            traindata = finaltraindata[:, trainnum]
            # 计算并存储测试数据与训练数据之间的距离
            distances.append(linalg.norm(testdata - traindata))
            trainnum = trainnum + 1
        #寻找最近的训练数据的下标
        minindex = distances.index(min(distances))
        #判断预测的下标与所给的下标是否相同
        if(trainlabel[minindex] == testlabel[testnum]):
            isright.append(1)
        else:
            isright.append(0)
        testnum = testnum + 1

    #计算正确率
    count = 0
    for tag in isright:
        if tag == 1:
            count = count + 1
    accuracy = float(count) / len(isright)

    return accuracy