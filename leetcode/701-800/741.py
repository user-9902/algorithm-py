"""
@title:      741. 摘樱桃
@difficulty: 困难
@importance: 4/5
@tags:       dp
"""
from typing import List
from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        @tags:              dp 💲浮点精度
        @time complexity:   O(n^3)
        @space complexity:  O(n^3)
        @description:       不能两次dp计算，存在反例。需要一次dp考虑两个点的情况
        """
        n = len(grid)

        @cache
        def dfs(step, i, j):
            iy = step - i
            jy = step - j

            if i > n - 1 or j > n - 1 or iy > n - 1 or jy > n - 1:
                return -float("inf")
            if grid[i][iy] == -1 or grid[j][jy] == -1:
                return -float("inf")

            val = grid[i][iy] + grid[j][jy]
            if i == j and iy == jy:
                val -= grid[i][iy]
            if i == n - 1 and j == n - 1 and iy == n - 1 and jy == n - 1:
                return val

            return (
                max(
                    dfs(step + 1, i, j),
                    dfs(step + 1, i + 1, j),
                    dfs(step + 1, i, j + 1),
                    dfs(step + 1, i + 1, j + 1),
                )
                + val
            )

        return max(dfs(0, 0, 0), 0)


Solution().cherryPickup([[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [
    1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1]])
