#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import random

'''
函数功能：

数据结构：

'''

def samplingForCrossValidation(datanum, foldnum):
    trainindices = []
    testindices = []
    numperfold = round(datanum / foldnum)
    list = [i for i in range(datanum)]
    for i in range(foldnum - 1):
        temp = random.sample(list, numperfold)
        testindices.append(temp)
        tempall = [k for k in range(datanum)]
        for j in temp:
            list.remove(j)
            tempall.remove(j)
        trainindices.append(tempall)
    testindices.append(list)
    tempall = [i for i in range(datanum)]
    for i in list:
        tempall.remove(i)
    trainindices.append(tempall)
    return trainindices, testindices