#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ReadFile
import ComputeTFIDF
import TransToSparse
import WriteFile

path = raw_input(u'请输入文件路径: ')
print u'处理中...'
#用于存储提取词干、去除停词之后所有的单词
wordlist = set()
#用于存储所有paper的目录及名字
paperdir = {}
#用于存储所有paper的单词统计
paperlist = {}
#读取paper数据
ReadFile.readFile(path, wordlist, paperdir, paperlist)
#用于存储wordlist由set转化为list后的结果，单词按字典序排列
wlist = []
#用于存储最终计算出的TFIDF结果
finalresult = {}
#计算TFIDF
ComputeTFIDF.computeTFIDF(wordlist, paperdir, paperlist, wlist, finalresult)
#用于存储结果的稀疏表示
sparseresult = {}
#转化为稀疏矩阵
TransToSparse.transToSparse(finalresult, sparseresult)
#将结果写入当前目录下的'results.txt'文件中
WriteFile.writeFile(paperdir, sparseresult)
