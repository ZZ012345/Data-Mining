#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import ReadFile
import LearnPCAConjMat
import DimReduction
import PredictLabel
import ISOMAP

trainfilename = 'sonar-train.txt'
testfilename = 'sonar-test.txt'
#读取文件
trainmatdata, trainlabel = ReadFile.readFile(trainfilename)
testmatdata, testlabel = ReadFile.readFile(testfilename)

dimension = 10 #降维目标维数
'''
evals ,evcts = LearnPCAConjMat.learnPCAConjMat(trainmatdata) #根据训练集学习PCA投影矩阵
finaltraindataPCA, finaltestdataPCA = DimReduction.dimReduction(trainmatdata, testmatdata, evcts, dimension) #对训练集和测试集数据进行降维
accuracyPCA = PredictLabel.predictLabel(finaltraindataPCA, trainlabel, finaltestdataPCA, testlabel) #对测试数据集进行标签预测，计算正确率
print accuracyPCA

u, s, v = linalg.svd(trainmatdata) #根据训练集学习SVD投影矩阵
finaltraindataSVD, finaltestdataSVD = DimReduction.dimReduction(trainmatdata, testmatdata, u, dimension) #对训练集和测试集数据进行降维
accuracySVD = PredictLabel.predictLabel(finaltraindataSVD, trainlabel, finaltestdataSVD, testlabel) #对测试数据集进行标签预测，计算正确率
print accuracySVD
'''
k = 30 #k-NN参数k
ISOMAP.ISOMAP(trainmatdata, testmatdata, k)
