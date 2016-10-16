#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import ReadFile
import LearnPCAConjMat
import DimReduction
import PredictLabel
import ISOMAP

file = raw_input(u'请选择数据集，\'1\'代表sonar，\'2\'代表splice：')
fchoice = True
while(fchoice):
    if(file == '1'):
        trainfilename = 'sonar-train.txt'
        testfilename = 'sonar-test.txt'
        fchoice = False
    elif(file == '2'):
        trainfilename = 'splice-train.txt'
        testfilename = 'splice-test.txt'
        fchoice = False
    else:
        file = raw_input(u'输入错误，请重新选择：')
#读取文件
trainmatdata, trainlabel = ReadFile.readFile(trainfilename)
testmatdata, testlabel = ReadFile.readFile(testfilename)

dimension = raw_input(u'请输入降维的目标维数：')
dchoice = True
while(dchoice):
    try:
        dimension = int(dimension)
        if(dimension > 0):
            dchoice = False
        else:
            dimension = raw_input(u'目标维数必须为正，请重新输入：')
    except ValueError:
        dimension = raw_input(u'输入错误，请重新输入：')

#PCA
evals ,evcts = LearnPCAConjMat.learnPCAConjMat(trainmatdata) #根据训练集学习PCA投影矩阵
finaltraindataPCA, finaltestdataPCA = DimReduction.dimReduction(trainmatdata, testmatdata, evcts, dimension) #对训练集和测试集数据进行降维
accuracyPCA = PredictLabel.predictLabel(finaltraindataPCA, trainlabel, finaltestdataPCA, testlabel) #对测试数据集进行标签预测，计算正确率
print u'PCA降维的正确率为：', accuracyPCA

#SVD
u, s, v = linalg.svd(trainmatdata) #根据训练集学习SVD投影矩阵
finaltraindataSVD, finaltestdataSVD = DimReduction.dimReduction(trainmatdata, testmatdata, u, dimension) #对训练集和测试集数据进行降维
accuracySVD = PredictLabel.predictLabel(finaltraindataSVD, trainlabel, finaltestdataSVD, testlabel) #对测试数据集进行标签预测，计算正确率
print u'SVD降维的正确率为：', accuracySVD

#ISOMAP
k = 6 #k-NN参数k
type = 'dijkstra' #最短距离算法类型，可以选择'dijkstra'或'floyd'
result = ISOMAP.isomap(trainmatdata, testmatdata, k, type, dimension) #对训练集和测试集数据进行降维
if(size(result) != 0):
    finaltraindataISOMAP = result[:, 0: size(trainmatdata, 1)]
    finaltestdataISOMAP = result[:, size(trainmatdata, 1): (size(trainmatdata, 1) + size(testmatdata, 1))]
    accuracyISOMAP = PredictLabel.predictLabel(finaltraindataISOMAP, trainlabel, finaltestdataISOMAP, testlabel) #对测试数据集进行标签预测，计算正确率
    print u'ISOMAP降维的正确率为：', accuracyISOMAP
else:
    print u'ISOMAP降维失败'