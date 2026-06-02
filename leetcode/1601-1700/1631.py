"""
@title:      1631. 最小体力消耗路径
@difficulty: 中等
@importance: 5/5
@tags:       并查集 二分 最小生成树
"""


from typing import List
from heapq import heappop, heappush

arr = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Union:
    def __init__(self, size):
        self.f = [i for i in range(size)]

    def father(self, i):
        res = self.f[i]
        return res if res == i else self.father(res)

    def union(self, x, y):
        fx, fy = self.father(x), self.father(y)
        if fx != fy:
            self.f[fx] = fy


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        @tags:              并查集
        @time complexity:   O(mnlog(mn))
        @space complexity:  O(mn)
        @description:
        """
        n, m = len(heights), len(heights[0])
        union = Union(n * m)
        edges = []
        for i in range(n):
            for j in range(m):
                if i < n - 1:
                    edges.append(
                        [
                            abs(heights[i][j] - heights[i + 1][j]),
                            i * m + j,
                            (i + 1) * m + j,
                        ]
                    )
                if j < m - 1:
                    edges.append(
                        [
                            abs(heights[i][j] - heights[i][j + 1]),
                            i * m + j,
                            i * m + j + 1,
                        ]
                    )
        if len(edges) == 0:
            return 0
        edges.sort()
        for v, a, b in edges:
            union.union(a, b)
            if union.father(0) == union.father(n * m - 1):
                return v

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        @tags:              最短路
        @time complexity:   O(mnlog(mn))
        @space complexity:  O(mn)
        @description:       Dijkstra
        """
        n, m = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        f = [[float('inf')] * m for _ in range(n)]
        s = [[False] * m for _ in range(n)]

        q = [(0, 0, 0)]
        f[0][0] = 0
        s[0][0] = False

        while q:
            v, i, j = heappop(q)
            if s[i][j]:
                continue
            if i == n - 1 and j == m - 1:
                return v

            s[i][j] = True
            for a, b in dirs:
                if (
                    -1 < i + a < n
                    and -1 < j + b < m
                    and abs(heights[i][j] - heights[i + a][j + b]) <= f[i + a][j + b]
                ):
                    f[i + a][j + b] = max(
                        v,
                        abs(heights[i][j] - heights[i + a][j + b])
                    )
                    heappush(q, (f[i + a][j + b], i + a, j + b))
