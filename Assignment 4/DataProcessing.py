#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import LogisticRegression
import RidgeRegression

case = 2
if(case == 0):
    trainfile = 'dataset1-a9a-training.txt'
    traindata, trainlabel = ReadFile.readFile(trainfile)
    testfile = 'dataset1-a9a-testing.txt'
    testdata, testlabel = ReadFile.readFile(testfile)
    LogisticRegression.logisticRegression(traindata, trainlabel, testdata, testlabel, lamda = 0, gamma = 0.008)
elif(case == 1):
    trainfile = 'covtype-training.txt'
    traindata, trainlabel = ReadFile.readFile(trainfile)
    testfile = 'covtype-testing.txt'
    testdata, testlabel = ReadFile.readFile(testfile)
    LogisticRegression.logisticRegression(traindata, trainlabel, testdata, testlabel, lamda = 0, gamma = 0.008)
elif(case == 2):
    trainfile = 'dataset1-a9a-training.txt'
    traindata, trainlabel = ReadFile.readFile(trainfile)
    testfile = 'dataset1-a9a-testing.txt'
    testdata, testlabel = ReadFile.readFile(testfile)
    RidgeRegression.ridgeRegression(traindata, trainlabel, testdata, testlabel, lamda = 0.01, gamma = 0.008)
else:
    trainfile = 'covtype-training.txt'
    traindata, trainlabel = ReadFile.readFile(trainfile)
    testfile = 'covtype-testing.txt'
    testdata, testlabel = ReadFile.readFile(testfile)
    RidgeRegression.ridgeRegression(traindata, trainlabel, testdata, testlabel, lamda = 0, gamma = 0.008)