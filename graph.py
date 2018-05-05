#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Pis
@license: Apache Licence 
@software: PyCharm
@file: graph.py
@time: 2018/4/1 14:44
"""
G = [
    {1, 2, 3},
    {0, 4, 6},
    {0, 3},
    {0, 2, 4},
    {1, 3, 5, 6},
    {4, 7},
    {1, 4},
    {5}
]


def dfs(G, v, visited=set()):
    print(v)
    visited.add(v)
    for u in G[v]:
        if u not in visited:
            dfs(G, u, visited)


def dfsIter(G, v):
    visited = set()
    s = [v]
    while s:
        u = s.pop()
        if u not in visited:
            print(u)
            visited.add(u)
            s.extend(G[u])


from collections import deque


def bfs(G, v):
    q = deque([v])
    visited = {v}
    while q:
        u = q.popleft()
        print(u)
        for w in G[u]:
            if w not in visited:
                q.append(w)
                visited.add(w)


dfs(G, 1)


#最小生成树

G = [
    {1: 28, 5: 10},
    {0: 28, 2: 16, 6: 14},
    {1: 16, 3: 12},
    {2: 12, 4: 22, 6: 18},
    {3: 22, 5: 25, 6: 24},
    {0: 10, 4: 25},
    {1: 14, 3: 18, 4: 24},
]


import heapq


def prim(G):
    n = len(G)
    v = 0
    s = {v}
    edges = []
    res = []
    for _ in range(n-1):
        for u, w in G[v].items():
            heapq.heappush(edges, (w, v, u))
        while edges:
            w, p, q = heapq.heappop(edges)
            if q not in s:
                s.add(q)
                res.append(((p, q), w))
                v = q
                break
        else:
            raise Exception("not connected graph")
    return res


res = prim(G)
print(sum([x[1] for x in res]))


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


G = {
    'C1': ['C3', 'C8'],
    'C2': ['C3', 'C4', 'C5'],
    'C3': ['C4'],
    'C4': ['C6', 'C7'],
    'C5': ['C6'],
    'C6': [],
    'C7': [],
    'C8': ['C9'],
    'C9': ['C7']
}


def topsort(G):
    indegrees = {v: 0 for v in G}
    for al in G.values():
        for v in al:
            indegrees[v] += 1
    q = [v for v in G if indegrees[v] == 0]
    i = 0
    while i < len(q):
        for v in G[q[i]]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                q.append(v)
        i += 1
    return q if i == len(G) else None

