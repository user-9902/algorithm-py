"""
@title:      879. 盈利计划
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from functools import cache
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        @tags:              递归
        @time complexity:   O(nmk)
        @space complexity:  O(nmk)  ❌超内存限制
        @description:       01背包   多条件限制 一个>= 一个<=
        """
        MOD = 10**9 + 7

        @cache
        def dfs(i, n, val):
            if i < 0:
                return 1 if val >= minProfit else 0
            if n < group[i]:
                return dfs(i - 1, n, val)
            else:
                return (
                    dfs(i - 1, n, val) +
                    dfs(i - 1, n - group[i], val + profit[i])
                ) % MOD

        return dfs(len(group) - 1, n, 0)

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        @tags:              递推
        @time complexity:   O(nmk)
        @space complexity:  O(nmk)   状态压缩同01背包
        @description:       01背包 高一维的01背包
        """
        MOD = 10**9 + 7
        m = len(group)

        f = [[[0] * (minProfit + 1) for j in range(n + 1)]
             for i in range(m + 1)]
        f[0][0][0] = 1

        for i in range(m):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    # 当前不选
                    f[i + 1][j][k] = f[i][j][k]
                    # 当前选
                    if j >= group[i]:
                        # 选完当前的子问题 f[i][j - group[i]][k - profit[i]]
                        new_profit = max(0, k - profit[i])
                        f[i + 1][j][k] += f[i][j - group[i]][new_profit]
                        f[i + 1][j][k] %= MOD
        return sum(f[m][j][minProfit] for j in range(n + 1)) % MOD
