#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Pis
@license: Apache Licence 
@software: PyCharm
@file: test.py
@time: 2018/5/2 16:06
"""
import heapq

a, b, c, d, e, f = range(6)
G = {
    a: {b: 2, c: 1, d: 4, f: 10},
    b: {a: 2, c: 4, e: 3},
    c: {a: 1, b: 4, d: 2, f: 8},
    d: {a: 4, c: 2, e: 1},
    e: {b: 3, d: 1, f: 7},
    f: {a: 10, c: 8, e: 7},
}

#最短路径

def dijkstra(G, s):
    inf = float("inf")
    D = {v: inf for v in G}
    D[s] = 0 #点与原点的总距离
    P = {} #来源
    S = {s}
    q = []
    v = s
    for _ in range(len(G) - 1):
        for u, w in G[v].items():
            d = D[v] + G[u][v]
            if D[u] > d:
                D[u] = d
                P[u] = v
                heapq.heappush(q, (d, u))
        while q:
            _, v = heapq.heappop(q)
            if v not in S:
                S.add(v)
                break
        else:
            break
    return D, P


A,B=dijkstra(G,0)
print(A,B)
