#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Pis
@license: Apache Licence 
@software: PyCharm
@file: list.py
@time: 2018/3/31 13:20
"""
LEFT = {'{', '[', '('}
RIGHT = {'}', ']', ')'}


def match(expr):
    s = []
    for c in expr:
        if c in LEFT:
            s.append(c)
        elif c in RIGHT:
            if not s:
                return False
            if not 1 <= ord(c) - ord(s[-1]) <= 2:
                return False
            s.pop()
    return not s


print(match('{{}{}{}{'))


def initMaze():
    maze = [[0]*7 for _ in range(5+2)]
    walls = [(1, 3), (2, 1), (2, 5), (3, 3), (3, 4), (4, 2), (4, 3), (5, 4),]
    for i in range(5+2):
        maze[i][0] = maze[i][-1] = 1
        maze[0][i] = maze[-1][i] = 1
    for i, j in walls:
        maze[i][j] = 1
    return maze


def path(maze, start, end):
    i, j = start
    ei, ej = end
    s = [(i, j)]
    maze[i][j] = 1
    while s:
        i, j = s[-1]
        if (i, j) == (ei, ej):
            break
        for di, dj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            if maze[i+di][j+dj] == 0:
                maze[i+di][j+dj] = 1
                s.append((i+di, j+dj))
                break
        else:
            s.pop()
    return s


maze = initMaze()
print(path(maze, (1, 1), (5, 5)))

operators = {
    '+': lambda op1, op2: op1+op2,
    '-': lambda op1, op2: op1-op2,
    '*': lambda op1, op2: op1*op2,
    '/': lambda op1, op2: op1/op2,
 }


def evalPostfix(e):
    tokens = e.split()
    s = []
    for token in tokens:
        if token.isdigit():
            s.append(int(token))
        elif token in operators:
            f = operators[token]
            op2 = s.pop()
            op1 = s.pop()
            s.append(f(op1, op2))
    return s.pop()


print(evalPostfix("2 3 4 * +"))


def knapsack(t, w):
    n = len(w)
    s = []
    k = 0
    while s or k < n:
        while t > 0 and k < n:
            if t >= w[k]:
                s.append(k)
                t -= w[k]
            k += 1
        if t == 0:
            print(s)

        # 回数过程
        k = s.pop()
        t += w[k]
        k += 1


knapsack(10, (1, 8, 4, 3, 5, 2))


if __name__ == "__main__":
    pass

