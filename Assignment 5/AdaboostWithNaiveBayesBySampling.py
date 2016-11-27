#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import NaiveBayes
import math

'''
函数功能：

数据结构：

'''

def adaboostWithNaiveBayesBySampling(data, label, datatype):
    datadim, datanum = shape(data)
    classifiersweight = [] #分类器权重
    classifiers = [] #每个分类器中的每个样本对应的权重，即数据分布
    classifiersdata =[] #每个分类器中的数据
    classifierslabel = [] #每个分类器中数据对应的标签
    sampleweights = [1 / datanum] * datanum #初始样本权重，即初始数据分布
    classifiers.append([i for i in sampleweights])
    classifiersdata.append(data)
    classifierslabel.append(label)
    result, errorrate = NaiveBayes.naiveBayes(data, label, data, label, datatype) #用原始数据集训练第一个贝叶斯分类器
    if(errorrate > 0.5):
        print('初始分类器不满足要求')
        return
    cweight = 0.5 * math.log((1 - errorrate) / errorrate, math.e) #初始分类器权重
    classifiersweight.append(cweight)
    #更新样本分布
    for i in range(datanum):
        sampleweights[i] = sampleweights[i] * math.exp(-cweight * label[i] * result[i])
    sumweights = sum(sampleweights)
    for i in range(datanum): #规范化
        sampleweights[i] = sampleweights[i] / sumweights
    classifiers.append([i for i in sampleweights])
    print('第 1 个分类器的误差：', errorrate)

    #重复训练分类器
    T = 5
    for iteration in range(1, T):
        errorrate = 1
        while(errorrate >= 0.5): #采用重采样策略
            samplingdata, samplinglabel, indices = sampling(data, label, sampleweights, datanum) #采样
            #result, errorrate = NaiveBayes.naiveBayes(samplingdata, samplinglabel, samplingdata, samplinglabel, datatype) #训练新的贝叶斯分类器
            result, errorrate = NaiveBayes.naiveBayes(data, label, samplingdata, samplinglabel, datatype)
        print('第', iteration + 1, '个分类器的误差：', errorrate)
        classifiersdata.append(samplingdata)
        classifierslabel.append(samplinglabel)
        cweight = 0.5 * math.log((1 - errorrate) / errorrate, math.e)
        classifiersweight.append(cweight)
        #更新样本分布
        for i in range(datanum):
            #try:
                #sampleweights[i] = sampleweights[i] * math.exp(-cweight * label[i] * result[indices.index(i)])
            #except ValueError:
                #pass
            sampleweights[i] = sampleweights[i] * math.exp(-cweight * label[i] * result[i])
        sumweights = sum(sampleweights)
        for i in range(datanum):  #规范化
            sampleweights[i] = sampleweights[i] / sumweights
        classifiers.append([i for i in sampleweights])

    return classifiersweight, classifiers, classifiersdata, classifierslabel


def sampling(data, label, weight, size): #采样函数，data表示待采样的数据，label为对应标签，weight存储每个样本的权重，即样本分布，size为采样的目标样本量
    indices = [] #采样后的样本下标
    for i in range(size): #采样
        rannum = random.random()
        count = 0
        index = 0
        while(count < rannum):
            count += weight[index]
            index += 1
        if(index == 0):
            indices.append(0)
        else:
            indices.append(index - 1)
    samplingdata = data[:, indices]
    samplinglabel = [label[i] for i in indices]
    return samplingdata, samplinglabel, indices


def test(sample, samplelabel, classifiersweight, classifiersdata, classifierslabel, datatype):
    samplenum = size(sample, axis=1)
    finalresult = [0] * samplenum
    classifiersnum = len(classifiersweight)
    for i in range(classifiersnum):
        result, errorrate = NaiveBayes.naiveBayes(sample, samplelabel, classifiersdata[i], classifierslabel[i], datatype)
        for j in range(samplenum):
            finalresult[j] = finalresult[j] + classifiersweight[i] * result[j]
    for i in range(samplenum):
        if(finalresult[i] > 0):
            finalresult[i] = 1
        elif(finalresult[i] < 0):
            finalresult[i] = -1
    errorrate = NaiveBayes.calculateErrorRate(finalresult, samplelabel)
    return errorrate