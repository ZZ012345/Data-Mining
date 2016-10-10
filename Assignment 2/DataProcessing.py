#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ReadFile
import LearnConjMat
import ComputePCA
import PredictLabel

trainfilename = 'sonar-train.txt'
testfilename = 'sonar-test.txt'
#读取文件
trainmatdata, trainlabel = ReadFile.readFile(trainfilename)
testmatdata, testlabel = ReadFile.readFile(testfilename)
#根据训练集学习投影矩阵
evals ,evcts = LearnConjMat.learnConjMat(trainmatdata)
#对训练集和测试集数据进行降维
finaltraindata, finaltestdata = ComputePCA.computePCA(trainmatdata, testmatdata, evcts, dimension = 10)
#对测试数据集进行标签预测，计算正确率
accuracy = PredictLabel.predictLabel(finaltraindata, trainlabel, finaltestdata, testlabel)
print accuracy