#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Pis
@license: Apache Licence 
@software: PyCharm
@file: tree.py
@time: 2018/4/1 10:45
"""


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def creatTree():
    A, B, C, D, E, F, G, H, I = [TreeNode(i) for i in 'ABCDEFGHI']
    A.left = B
    A.right = C
    B.right = D
    C.right = F
    C.left = E
    E.left = G
    F.left = H
    F.right = I
    return A


def preOrder(node):
    if node is None:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)


def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data)
    inOrder(node.right)


def preOrderIter(root):
    s = []
    node = root
    while True:
        while node:
            print(node)
            s.append(node)
            node = node.left

        if not s:
            break
        node = s.pop().right


from collections import deque


def levelOrder(node):
    q = deque([node])
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def depth(node):
    if node is None:
        return 0
    dl = depth(node.left)
    dr = depth(node.right)
    return max(dl, dr)+1


def depth2(node):
    q = deque([node, 1])
    while q:
        node, d = q.popleft()
        # print( node)
        if node.left:
            q.append(node.left, d+1)
        if node.right:
            q.append(node.right, d+1)
    return d


def copyTree(node):
    if node is None:
        return None
    lt = copyTree(node.left)
    rt = copyTree(node.right)
    return TreeNode(node.data, lt, rt)


def count(n):
    #root:1
    #left:k
    #right:n-1-k

    s = cache.get(n, 0)
    if s:
        return s
    for k in range(n):
        s += count(k)*count(n-1-k)
    cache[n] = s
    return s


cache = {0: 1}

print(count(4))


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def search(self, k):
        node, _ = self._search(k)
        return node

    def _search(self, k):
        parent = None
        node = self.root
        while node and node.data != k:
            parent = node
            if k < node.data:
                node = node.left
            else:
                node = node.right
        return node, parent

    def insert(self, k):
        node, parent = self._search(k)
        if node:
            return
        node = TreeNode(k)
        if parent is None:
            self.root = node
        elif parent.data > k:
            parent.left = node
        else:
            parent.right = node
        return

    def delete(self, k):
        node, parent = self._search(k)
        if not node:
            return
        if node and not parent:
            self.root = None
        if parent.data > node.data:
            parent.left = None
            node.__del__()
        else:
            parent.right = None
            node.__del__()


if __name__ == "__main__":
    root = creatTree()
    #preOrder(root)
    inOrder(root)
