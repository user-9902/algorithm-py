"""
@title:      778. 水位上升的泳池中游泳
@difficulty: 中等
@importance: 5/5
@tags:       Kruskal 并查集
"""

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        @tags:              Kruskal
        @time complexity:   O(n)
        @space complexity:  O(n)
        """
        n = len(grid)
        f = [[True] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        f[0][0] = False
        while heap:
            curv, x, y = heapq.heappop(heap)
            if x == n - 1 and y == n - 1:
                return curv

            if x > 0 and f[x - 1][y]:
                heapq.heappush(heap, (max(curv, grid[x - 1][y]), x - 1, y))
                f[x-1][y] = False
            if x < n - 1 and f[x + 1][y]:
                heapq.heappush(heap, (max(curv, grid[x + 1][y]), x + 1, y))
                f[x+1][y] = False
            if y > 0 and f[x][y - 1]:
                heapq.heappush(heap, (max(curv, grid[x][y - 1]), x, y - 1))
                f[x][y-1] = False
            if y < n - 1 and f[x][y + 1]:
                heapq.heappush(heap, (max(curv, grid[x][y + 1]), x, y + 1))
                f[x][y+1] = False
        return -1

    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        @tags:              并查集
        @time complexity:   O(n)
        @space complexity:  O(n)
        """
        m, n = len(grid), len(grid[0])
        par = [i for i in range(m*n)]

        def find(x):
            if x == par[x]:
                return x
            return find(par[x])

        def un(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            par[ry] = rx

        def isc(x, y):
            return find(x) == find(y)
        edgs = []
        for i in range(m):
            for j in range(n):
                pos = i*n+j
                d = grid[i][j]
                if i+1 < m:
                    edgs.append((max(d, grid[i+1][j]), pos, pos+n))
                if j+1 < n:
                    edgs.append((max(d, grid[i][j+1]), pos, pos+1))
        edgs.sort(reverse=False)
        for d, x, y in edgs:
            un(x, y)
            if isc(0, m*n-1):
                return d
        return 0


Solution().swimInWater([[0, 2], [1, 3]])
