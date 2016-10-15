#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
函数功能：
将sparseresult写入当前目录下的results.txt文件中，如果没有该文件则创建一个
'''

def writeFile(paperdir, sparseresult):
    with open('results.txt', 'w') as f:
        #需写入的paper大类
        paperset = paperdir['7. Kernel Methods']
        papernum = 1
        mark = 0
        for paper in paperset:
            if (papernum != 1) and (mark == 0):
                f.write('\n\n')
            elif mark == 1:
                f.write('\n')
            papernum = papernum + 1
            f.write(paper)
            f.write(':\n')
            #提取稀疏表示
            result = sparseresult[paper]
            num = 1
            #用于标记是奇数位还是偶数位
            odd = True
            for a in result:
                if odd == True:
                    f.write(str(a))
                    f.write(': ')
                    odd = False
                else:
                    f.write(str(a))
                    f.write(', ')
                    odd = True
                num = num + 1
                #每输入5组数据换行
                if num == 11:
                    f.write('\n')
                    num = 1
                    mark = 1
                else:
                    mark = 0

    print u'写入结束'
    print u'程序运行结束'
