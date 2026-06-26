"""
@title:      188. 买卖股票的最佳时机 IV
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from typing import List
from math import inf
from functools import cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        @tags:              递归
        @time complexity:   O(nk)
        @space complexity:  O(nk)
        @description:       leetcode 122的变形题 加上了天数限制 见注释
        """
        n = len(prices)

        @cache
        # 第i天 第j次操作 当前是否持有
        def dfs(i, j, hold):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0

            if hold:
                #  持有 继续持有 买入
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            else:
                # 不持有 继续不持有 卖出
                return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])

        return dfs(n - 1, k, False)

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(nk)
        @space complexity:  O(nk)   状态来之上左方，压缩状态的时候从后向前即可
        @description:       
        """
        n = len(prices)
        # k + 2 i + 1 都是为了防止状态转移方程导致数组越界
        f = [[[-inf, -inf] for _ in range(k+2)] for _ in range(n+1)]

        for i in range(1, k+2):
            f[0][i][0] = 0

        for i, p in enumerate(prices):
            for j in range(1, k+2):
                f[i+1][j][0] = max(f[i][j+1][0], f[i][j][1] + p) # 不操作 or 卖出
                f[i+1][j][1] = max(f[i][j+1][1], f[i][j-1][0] - p) # 不操作 or 买入

        return f[-1][-1][0]
