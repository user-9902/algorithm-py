"""
@title:      427. 建立四叉树
@difficulty: 中等
@importance: 3/5
@tags:       dfs 业务题
"""
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        pre = [[0] * (n+1) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                pre[i][j+1] = pre[i][j] + grid[i][j]

        def dfs(l, r, t, b):
            sam = 0
            for i in range(t, b+1):
                sam += pre[i][r+1] - pre[i][l]
            if sam == (r-l + 1) * (b-t+1):
                return Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            elif sam == 0:
                return Node(val=0, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                row_m = (r+l) >> 1
                col_m = (b+t) >> 1
                return Node(val=None, isLeaf=False, topLeft=dfs(l, row_m, t, col_m), topRight=dfs(row_m+1, r, t, col_m), bottomLeft=dfs(l, row_m, col_m+1, b), bottomRight=dfs(row_m+1, r, col_m+1, b))

        return dfs(0, n-1, 0, n-1)
