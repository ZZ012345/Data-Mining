#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
从当前目录的filename文件中提取数据，返回特征矩阵和标签
数据结构：
特征矩阵每一列代表一个样例，数据类型为float，标签的数据结构为由str组成的list，每个样例都有一个与之对应的标签
'''

def readFile(filename):
    #打开文件
    with open('./' + filename, 'r') as f:
        data = []
        label = []
        #按行读取
        for line in f.readlines():
            #按逗号分隔提取数据
            linedata = line.strip().split(',')
            count = 0
            linelen = len(linedata)
            flinedata = []
            while count < linelen - 1:
                flinedata.append(float(linedata[count]))
                count = count + 1
            #存储标签
            label.append(linedata[count])
            #存储特征
            data.append(flinedata)

    return mat(data).T, label
