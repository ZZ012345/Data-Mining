#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

'''
函数功能：
计算TFIDF并将结果保存在finalresult中
数据结构：
finalresult为dict结构，其key为paper名，value为由所有单词对应TFIDF值组成的list
'''

def computeTFIDF(wordlist, paperdir, paperlist, wlist, finalresult):
    #将wordlist由set转化为list
    for word in wordlist:
        wlist.append(word)
    wlist.sort()

    #计算出现每个单词的paper数和总的paper数
    winpnum = []
    papernum = 0
    for word in wlist:
        num = 0
        for dirname in paperdir:
            paperset = paperdir[dirname]
            for paper in paperset:
                if word in paperlist[paper]:
                    num = num + 1
                papernum = papernum + 1
        winpnum.append(num)
    papernum = papernum / len(wlist)
    
    
    #计算TFIDF
    #按类别进行遍历
    for dirname in paperdir:
        #一个类别下所有的paper
        paperset = paperdir[dirname]
        #按paper进行遍历
        for paper in paperset:
            #用于存储TFIDF结果，数组顺序对应wlist中的单词顺序
            tfidf = []
            num = 0
            for word in wlist:
                #wlist中的单词不在paper中
                if not (word in paperlist[paper]):
                    tfidf.append(0)
                #wlist中的单词在paper中，计算该单词对应的TFIDF
                else:
                    wnum = paperlist[paper][word]
                    tf = 1 + math.log10(wnum)
                    idf = math.log10(papernum / winpnum[num])
                    tfidf.append(tf * idf)
                num = num +1
            finalresult[paper] = tfidf

    print u'TD-IDF计算结束'
