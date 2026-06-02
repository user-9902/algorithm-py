"""
name:       576. 出界的路径数
difficulty: 简单
importance: 3/5
tags:       记忆化搜索 
"""
from functools import cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        @tags:              binary_search sort
        @time complexity:   O(n^4)
        @space complexity:  O(n)
        """

        MOD = 10**9 + 7

        @cache
        def dfs(x, y, step):
            if step < 0:
                return 0
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            else:
                return (
                    dfs(x - 1, y, step - 1)
                    + dfs(x + 1, y, step - 1)
                    + dfs(x, y - 1, step - 1)
                    + dfs(x, y + 1, step - 1)
                ) % MOD

        return dfs(startRow, startColumn, maxMove)
