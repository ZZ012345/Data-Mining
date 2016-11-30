#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import SamplingForCrossValidation
import AdaboostWithNaiveBayesBySampling
import AdaboostWithNaiveBayes

filename = 'breast-cancer-assignment5.txt'
#filename = 'german-assignment5.txt'
data, datatype, label = ReadFile.readFile(filename)
trainindices, testindices = SamplingForCrossValidation.samplingForCrossValidation(len(label), 10)

runtimes = 10
errorrates = []
for testnum in range(10):
    traindata = data[:, trainindices[testnum]]
    trainlabel = [label[i] for i in trainindices[testnum]]
    #由于采样具有随机性，在训练集上多次采样并训练，用训练集测试，选择误差最小的贝叶斯分类器
    storage = []
    results = []
    for i in range(runtimes):
        classifiersweight, classifiers, classifiersdata, classifierslabel = AdaboostWithNaiveBayesBySampling.adaboostWithNaiveBayesBySampling(traindata, trainlabel, datatype)
        storage.append(classifiersweight)
        storage.append(classifiers)
        storage.append(classifiersdata)
        storage.append(classifierslabel)
        if(len(classifiersweight) != 0):
            finalerrorrate = AdaboostWithNaiveBayesBySampling.test(traindata, trainlabel, classifiersweight, classifiersdata, classifierslabel, datatype)
            results.append(finalerrorrate)
            print('测试误差：', finalerrorrate)
        else:
            results.append(1)
            print('训练提前终止')
        print('----------------------------------------')
    print('最低测试误差：', min(results))
    index = results.index(min(results))
    finalclassifiersweight = storage[4 * index]
    finalclassifiers = storage[4 * index + 1]
    finalclassifiersdata = storage[4 * index + 2]
    finalclassifierslabel = storage[4 * index + 3]
    #对测试集进行测试
    testdata = data[:, testindices[testnum]]
    testlabel = [label[i] for i in testindices[testnum]]
    errorrate = AdaboostWithNaiveBayesBySampling.test(testdata, testlabel, finalclassifiersweight, finalclassifiersdata, finalclassifierslabel, datatype)
    print('第', testnum + 1, '次交叉验证的错误率为：', errorrate)
    print('****************************************')
    errorrates.append(errorrate)
meanerrorrate = mean(array(errorrates))
stderrorrate = std(array(errorrates))
print('交叉验证的平均错误率为：', meanerrorrate)
print('交叉验证错误率的标准差为：', stderrorrate)