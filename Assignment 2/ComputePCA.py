#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

'''
函数功能：
根据输入的降维的目标维数对训练和测试数据进行降维，返回降维后的结果，目标维数是dimension
数据结构：
返回的降维结果矩阵中的每一列代表一个降维结果，与输入数据一一对应
'''

def computePCA(trainmatdata, testmatdata, evcts, dimension):
    if dimension < 1 or dimension > size(evcts, 0):
        print u'输入维数不合法'
        return
    return evcts[:, 0:dimension].T * trainmatdata, evcts[:, 0:dimension].T * testmatdata