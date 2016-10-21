#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile
import  Kmeans

filename = 'german.txt'
data, label = ReadFile.readFile(filename) #读取数据
clusters = Kmeans.kmeans(data, 2)
print clusters