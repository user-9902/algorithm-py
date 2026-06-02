"""
name:       200. 岛屿数量
difficulty: 简单
importance: 3/5
tags:       bfs 中心扩散
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        @tags:              bfs 中心扩散
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       bfs模拟感染过程即可
        """
        n = len(grid)
        m = len(grid[0])

        stack = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    stack.append([i, j])
        res = 0
        i = 0
        direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # 栈 bfs
        while i < len(stack):
            nxt_i = len(stack)
            for k in range(i, nxt_i):
                a, b = stack[k]
                for x, y in direc:
                    if -1 < a + x < n and -1 < b + y < m and grid[a + x][b + y] == 1:
                        grid[a + x][b + y] = 2
                        stack.append([a + x, b + y])
            if len(stack) > i+1:  # 有可能本轮无橘子可感染
                res += 1
            i = nxt_i

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return res
