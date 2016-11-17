#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：

数据结构：

'''

def naiveBayes(sample, data, datatype, label):
    datadim, datanum = shape(data)
    #统计每个类别的样本数量
    classnum = {}
    for i in range(datanum):
        if(label[i] not in classnum):
            classnum[label[i]] = 1
        else:
            classnum[label[i]] = classnum[label[i]] + 1
    print(classnum)
    #统计各类别下各属性的情况
    info = []
    diffnum = [] #每个属性包含不同属性值的数量，仅适用于离散属性，连续属性取值0
    for i in range(datadim):
        if(datatype[i] == 1): #离散属性
            feature = {} #{类标1:{属性值:数量, 属性值:数量}, 类标2:{属性值:数量, 属性值:数量}}
            for classname in classnum:
                feature[classname] = {}
            featureset = set() #用于存储所有属性值，能够过滤相同属性值
            for j in range(datanum):
                featureset.add(data[i][j])
                if(data[i][j] not in feature[label[j]]):
                    feature[label[j]][data[i][j]] = 1
                else:
                    feature[label[j]][data[i][j]] = feature[label[j]][data[i][j]] + 1
            info.append(feature)
            diffnum.append(len(featureset))
        #else: #连续属性
        #   feature
    print(info)
    print(diffnum)
    #计算条件概率
    condprob = {} #{类标1:[属性1的条件概率, 属性2的条件概率], 类标1:[属性1的条件概率, 属性2的条件概率]}
    for classname in classnum:
        condprob[classname] = []
    for i in range(datadim):
        if(datatype == 1): #离散属性
            for classname in condprob:
                if(sample[i] in info[i][classname]):
                    condprob[classname].append(info[i][classname][sample[i]])