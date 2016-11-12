#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import LogisticRegression

filename = 'dataset1-a9a-training.txt'
data, label = ReadFile.readFile(filename)
LogisticRegression.logisticRegression(data, label)