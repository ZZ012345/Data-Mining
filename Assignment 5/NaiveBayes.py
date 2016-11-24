#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import math
import scipy.stats as ss

'''
函数功能：

数据结构：

'''

def naiveBayes(sample, samplelabel, data, label, datatype):
    datadim, datanum = shape(data)
    #统计每个类别的样本数量
    classnum = {}
    for i in range(datanum):
        if(label[i] not in classnum):
            classnum[label[i]] = 1
        else:
            classnum[label[i]] = classnum[label[i]] + 1

    #统计各属性在各类别下的情况
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
        else: #连续属性
            feature = {} #{类标1:[均值, 标准差], 类标2:[均值, 标准差]}
            tempfeature = {} #{类标1:[属性值1, 属性值2], 类标2:[属性值1, 属性值2]}
            for classname in classnum:
                feature[classname] = []
                tempfeature[classname] = []
            for j in range(datanum):
                tempfeature[label[j]].append(data[i][j])
            for classname in classnum:
                dataarray = array(tempfeature[classname])
                feature[classname].append(mean(dataarray)) #均值
                feature[classname].append(std(dataarray)) #标准差
            info.append(feature)
            diffnum.append(0)

    #对样本进行分类
    samplenum = size(sample, axis=1)
    result = []
    for k in range(samplenum):
        #计算条件概率
        condprob = {} #{类标1:[属性1的条件概率, 属性2的条件概率], 类标1:[属性1的条件概率, 属性2的条件概率]}
        for classname in classnum:
            condprob[classname] = []
        for i in range(datadim):
            if(datatype[i] == 1): #离散属性
                for classname in condprob:
                    featurenum = info[i][classname].get(sample[i][k], 0)
                    probability = (featurenum + 1) / (classnum[classname] + diffnum[i]) #拉普拉斯修正
                    condprob[classname].append(probability)
            else: #连续属性
                for classname in condprob:
                    featuremean = info[i][classname][0] #取均值
                    featurestd = info[i][classname][1] #取标准差
                    probability = ss.norm.pdf(sample[i][k], featuremean, featurestd) #正态分布下的概率
                    condprob[classname].append(probability)

        #计算属于每一类的概率
        classprob = {} #{类标1:属于类别1概率, 类标2:属于类别2的概率}
        for classname in condprob:
            problist = condprob[classname]
            probability = math.log((classnum[classname] + 1) / (datanum + len(classnum))) #拉普拉斯修正
            for prob in problist:
                probability = probability + math.log(prob) #取对数，防止下溢
            classprob[classname] = probability

        #选择概率最高的类别
        maxclass = [i for i in classprob.keys()][0]
        maxprob = classprob[maxclass]
        for classname in classprob:
            if(classprob[classname] > maxprob):
                maxclass = classname
                maxprob = classprob[classname]
        result.append(maxclass)

    errorrate = calculateErrorRate(result, samplelabel)

    return result, errorrate

def calculateErrorRate(label, truelabel):
    errornum = 0
    for i in range(len(label)):
        if(label[i] != truelabel[i]):
            errornum += 1
    return errornum / len(label)