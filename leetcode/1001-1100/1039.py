"""
@title:      1039. 多边形三角剖分的最低得分
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List
from math import inf
from functools import cache


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        @tags:              递归 区间dp
        @time complexity:   O(n^3)
        @space complexity:  O(n^2)
        @description:       确认三角形的两个点，遍历第三个点，被三个点切割的部分，则是相同的子问题
        """
        @cache
        def dfs(l, r):
            if r - l < 2:
                return 0

            res = inf
            for k in range(l + 1, r):
                res = min(
                    res,
                    dfs(l, k) + dfs(k, r) + values[l] * values[r] * values[k],
                )
            return res

        return dfs(0, len(values) - 1)

    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        @tags:              区间dp
        @time complexity:   O(n^3)
        @space complexity:  O(n^2)
        @description:       翻译成递推
        """
        n = len(values)

        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if j - i > 1:
                    f[i][j] = inf
                    for k in range(i + 1, j):
                        f[i][j] = min(
                            f[i][j],
                            f[i][k] + f[k][j] + values[i] *
                            values[j] * values[k],
                        )
        return f[0][n - 1]
