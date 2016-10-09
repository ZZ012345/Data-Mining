#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能
'''

def predictLabel(finaltraindata, trainlabel, finaltestdata, testlabel):
    traindatanum = size(finaltraindata, 1) #训练数据量
    trainlabelnum = len(trainlabel) #训练标签量
    testdatanum = size(finaltestdata, 1) #测试数据量
    testlabelnum = len(testlabel) #测试标签量
    testnum = 0
    while testnum < testdatanum:
        testdata = finaltestdata[:, testnum] #取测试数据
        distances = [] #用于存储测试数据与训练数据之间的距离
        trainnum = 0
        while trainnum < traindatanum:
