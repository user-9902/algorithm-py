"""
@title:      3148. 矩阵中的最大得分
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""


from typing import List
from math import inf


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        """
        @tags:              dp
        @time complexity:   O(mn)
        @space complexity:  O(mn)
        @description:       维护当前遍历节点的前缀最小值（前缀来着左侧或上侧）
        """
        # dp
        n, m = len(grid), len(grid[0])
        ans = -inf
        # 防止溢出
        f = [[inf] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                mn = min(f[i][j + 1], f[i + 1][j])
                if v - mn > ans:
                    ans = v - mn
                # 更新前缀最小值
                f[i + 1][j + 1] = min(mn, v)
        return ans
