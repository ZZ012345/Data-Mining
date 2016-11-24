#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import NaiveBayes
import AdaboostWithNaiveBayes

filename = 'breast-cancer-assignment5.txt'
#filename = 'german-assignment5.txt'
data, datatype, label = ReadFile.readFile(filename)
AdaboostWithNaiveBayes.adaboostWithNaiveBayes(data, label, datatype)