"""
name:       200. 岛屿数量
difficulty: 简单
importance: 3/5
tags:       bfs 中心扩散
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        @tags:              bfs 中心扩散
        @time complexity:   O(nm)
        @space complexity:  O(1)
        @description:       遍历二维数组，发现陆地（1）给这块陆地打上标记，去重，继续遍历
        """
        n = len(grid)
        m = len(grid[0])
        res = 0

        dig = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "-1"
                for x, y in dig:
                    if -1 < i + x < n and -1 < j + y < m:
                        bfs(i + x, j + y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res
