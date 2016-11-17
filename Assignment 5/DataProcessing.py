#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import NaiveBayes

filename = 'breast-cancer-assignment5.txt'
data, datatype, label = ReadFile.readFile(filename)
sample = data[:, 0]
NaiveBayes.naiveBayes(sample, data, datatype, label)