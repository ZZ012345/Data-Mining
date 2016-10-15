#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
函数功能：
将之前计算出的TFIDF结果转化为稀疏表示
数据结构：
sparseresult为dict结构，其key为paper名，value为list，该list的奇数位表示在非稀疏结果中对应的坐标，后一位表示其值
'''

def transToSparse(finalresult, sparseresult):
    #按paper进行遍历
    for paper in finalresult:
        #提取原始表示
        result = finalresult[paper]
        #用于存储稀疏表示
        sparse = []
        offset = 0
        for a in result:
            if a != 0:
                sparse.append(offset)
                sparse.append(a)
            offset = offset + 1
        sparseresult[paper] = sparse

    print u'稀疏表示转化结束'
