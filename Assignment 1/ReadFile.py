#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import nltk.stem

'''
函数功能：
读取路径path下的所有paper中的单词，把结果保存在wordlist中，
统计每个目录下的paper名字保存在paperdir中，并把每篇paper的单词统计结果保存在paperlist中
数据结构：
wordlist为set结构，由提取词干、去除停词之后的所有单词组成
paperdir为dict结构，其key为paper的大类名，value为由该类下所有paper名组成的list
paperlist为dict结构，其key为paper名，value同样是dict结构，key为单词，value为该paper中该单词对应的数量
'''

def readFile(path, wordlist, paperdir, paperlist):
    #用于存储所有paper的路径
    filelist = []
    #用于存储所有paper的名字
    filename = []
    #读取path下的文件夹
    folders = os.listdir(path)
    for folder in folders:
        #排除隐藏文件夹
        if folder[0] == '.':
            pass
        else:
            papername = []
            files = os.listdir(path + '/' + folder)
            for file in files:
                fnamelen = len(file)
                #排除非txt文件
                if file[fnamelen - 4: fnamelen] == '.txt':
                    filelist.append(path + '/' + folder + '/' + file)
                    filename.append(file)
                    papername.append(file)
            #将paper名字列表添加到对应目录下
            paperdir[folder] = papername
 
    papernum = 0
    stemprocessor = nltk.stem.SnowballStemmer('english')
    #提取停词表
    stopwords = set()
    for sw in nltk.corpus.stopwords.words('english'):
        stopwords.add(sw)
    #根据路径对所有paper做处理
    for filepath in filelist:
        #读取paper
        with open(filepath, 'r') as f:
            text = f.read()
        #用于存储paper的单词统计结果
        pwordlist = {}
        textlen = len(text)
        start = 0
        end = 1
        while end < textlen:
            if text[start].isalpha():
                while (end < textlen) and text[end].isalpha():
                    end = end + 1
            else:
                end = start
            #提取单词
            if (end != start + 1) and (end != start):
                #提取词干
                word = stemprocessor.stem(text[start : end].lower())
                #去除停词表中的词
                if not (word in stopwords):
                    word = word.encode('utf-8')
                    #添加到wordlist中
                    wordlist.add(word)
                    #更新pwordlist
                    if word in pwordlist:
                        pwordlist[word] = pwordlist[word] + 1
                    else:
                        pwordlist[word] = 1
                start = end + 1
                end = start + 1
            else:
                start = end + 1
                end = start + 1

        paperlist[filename[papernum]] = pwordlist 
        papernum = papernum + 1

    print u'读取论文总数为: ' + str(papernum)
    print u'读取单词总数为: ' + str(len(wordlist))
    print u'读取结束'
