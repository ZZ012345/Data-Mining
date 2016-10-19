#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

import ReadFile

filename = 'german.txt'
data, label = ReadFile.readFile(filename) #读取数据