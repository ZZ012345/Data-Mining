#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
从当前目录的filename文件中提取数据，返回样本矩阵、标签以及样本数据的每一维是离散还是连续的
数据结构：
样本矩阵每一列代表一个样本，数据类型为float，标签的数据结构为由int组成的list，每个样本都有一个与之对应的标签
用于存储样本每一维数值类型的数据为list结构，其中1表示该维是离散数值，0表示连续数值
'''

def readFile(filename):
    data = []
    label = []
    datatype = []
    #打开文件
    with open('./' + filename, 'r') as f:
        #读取第一行
        firstline = f.readline()
        firstlinedata = firstline.strip().split(',')
        for i in range(len(firstlinedata)):
            datatype.append(int(firstlinedata[i]))
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
            temp = int(float(linedata[count]))
            if(temp == 0):
                temp = -1
            label.append(temp)
            #存储特征
            data.append(flinedata)

    return array(data).T, datatype, label