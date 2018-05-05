#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Pis
@license: Apache Licence 
@software: PyCharm
@file: queue.py
@time: 2018/3/31 20:47
"""
from collections import deque


def yanghui(k):
    q = deque([1])
    for i in range(k):
        for _ in range(i):
            q.append(q.popleft()+q[0])
        q.append(1)
    return q


yanghui(10)


from collections import deque


def division(M, n):
    res = []
    q = deque(range(n))
    pre = n
    while q:
        cur = q.popleft()
        if pre >= cur:
            res.append([])
        for a in res[-1]:
            if M[cur][a]:
                q.append(cur)
                break
        else:
            res[-1].append(cur)
        pre = cur
    return res




N = 9
R = {
    (1, 4), (4, 8), (1, 8), (1, 7),
    (8, 3), (1, 0), (0, 5), (1, 5),
    (3, 4), (5, 6), (5, 2), (6, 2), (6, 4)
}
M = [[0] * N for _ in range(N)]
for i, j in R:
    M[i][j] = M[j][i] = 1


print(division(M, N))


def atob(a, b):
    q = deque([(a, 0)])
    checked = {a}

    while True:
        s, c = q.popleft()
        if s == b:
            break
        if s < b:
            if s+1 not in checked:
                q.append((s+1, c+1))
                checked.add(s+1)
            if s*2 not in checked:
                q.append((s*2, c+1))
                checked.add(s*2)
        if s > 0:
            if s-1 not in checked:
                q.append((s-1, c+1))
                checked.add(s-1)
    return c


print(atob(5, 8))
