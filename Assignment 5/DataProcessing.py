#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import AdaboostWithNaiveBayesBySampling
import AdaboostWithNaiveBayes

filename = 'breast-cancer-assignment5.txt'
#filename = 'german-assignment5.txt'
data, datatype, label = ReadFile.readFile(filename)
type = 1
if(type == 0):
    classifiersweight, classifiers, classifiersdata, classifierslabel = AdaboostWithNaiveBayesBySampling.adaboostWithNaiveBayesBySampling(data, label, datatype)
    finalerrorrate = AdaboostWithNaiveBayesBySampling.test(data, label, classifiersweight, classifiersdata, classifierslabel, datatype)
else:
    classifiersweight, classifiers, classifiersdata, classifierslabel = AdaboostWithNaiveBayes.adaboostWithNaiveBayes(data, label, datatype)
    finalerrorrate = AdaboostWithNaiveBayes.test(data, label, classifiersweight, classifiersdata, classifierslabel, datatype)
print('测试误差：', finalerrorrate)