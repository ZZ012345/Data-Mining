#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ReadFile
import Kmedoids
import KmedoidsForBigData
import FastKmedoids
import FastKmedoidsForBigData
import KmPurityGini
import SpectralClustering
import SpectralClusteringForBigData

file = raw_input(u'请选择数据集，\'1\'代表german，\'2\'代表mnist：')
fchoice = True
while(fchoice):
    if(file == '1'):
        filename = 'german.txt'
        k = 2 #聚类数为2
        fchoice = False
    elif(file == '2'):
        filename = 'mnist.txt'
        k = 10 #聚类数为10
        fchoice = False
    else:
        file = raw_input(u'输入错误，请重新选择：')

algorithm = raw_input(u'请选择聚类算法，\'1\'代表kmedoids，\'2\'代表spectral：')
achoice = True
while(achoice):
    if(algorithm == '1'):
        algorithmtype = 'kmedoids'
        achoice = False
    elif(algorithm == '2'):
        algorithmtype = 'spectral'
        achoice = False
    else:
        algorithm = raw_input(u'输入错误，请重新选择：')

data, label = ReadFile.readFile(filename) #读取数据
kmedoidstype = 'fast' #kmedoids算法类型，可以选择“fast”或“normal”
if(algorithmtype == 'kmedoids'): #kmedoids聚类
    if(kmedoidstype == 'normal'):
        clusters = Kmedoids.kmedoids(data, k)
    elif(kmedoidstype == 'fast'):
        clusters = FastKmedoidsForBigData.fastKmedoidsForBigData(data, k)
    print u'聚类结果：', clusters
    purity, giniindex = KmPurityGini.kmPurityGini(label, clusters, k)
    print 'purity: ', purity
    print 'gini index: ', giniindex
elif(algorithmtype == 'spectral'): #谱聚类
    n = raw_input(u'请输入knn算法的参数k：')
    n = int(n)
    clusters = SpectralClusteringForBigData.spectralClusteringForBigData(data, n, k, kmedoidstype)
    print u'聚类结果：', clusters
    purity, giniindex = KmPurityGini.kmPurityGini(label, clusters, k)
    print 'purity: ', purity
    print 'gini index', giniindex