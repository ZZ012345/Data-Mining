#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
根据输入的降维投影矩阵和目标维数对训练以及测试数据进行降维，返回降维后的结果，投影矩阵是drmat，目标维数是dimension
数据结构：
返回的降维结果矩阵中的每一列代表一个降维结果，与输入数据一一对应
'''

def dimReduction(trainmatdata, testmatdata, drmat, dimension):
    if dimension < 1 or dimension > size(drmat, 0):
        print u'输入维数不合法'
        return
    #计算并返回降维结果
    return drmat[:, 0:dimension].T * trainmatdata, drmat[:, 0:dimension].T * testmatdata