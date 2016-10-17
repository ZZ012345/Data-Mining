#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import heappush, heappop

'''
函数功能：
单源最短路径算法，计算连接权重图graph中第start个节点到其他所有节点之间的最短距离
数据结构：
输入的graph为嵌套dict的dict结构，返回用于存放最短距离的list结构数据
'''

def dijkstra_fast(graph, start):
    A = [None] * len(graph)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    # to give same result as original, assign zero distance to unreachable vertices
    return [0 if x is None else x for x in A]