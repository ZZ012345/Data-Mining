#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
从当前目录的filename文件中提取数据，返回样本矩阵和标签
数据结构：
样本矩阵每一列代表一个样本，数据类型为float，标签的数据结构为由int组成的list，每个样本都有一个与之对应的标签
'''

def readFile(filename):
    data = []
    label = []
    #打开文件
    with open('./' + filename, 'r') as f:
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
            label.append(int(linedata[count]))
            #存储特征
            data.append(flinedata)

    return array(data).T, label