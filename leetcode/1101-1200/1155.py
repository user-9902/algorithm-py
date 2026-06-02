"""
@title:      1155. 掷骰子等于目标和的方法数
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        @tags:              递推
        @time complexity:   O(n*target)
        @space complexity:  O(n*target)  
        """
        MOD = 10**9 + 7

        @cache
        def dfs(i, t):
            if i == 0:
                return 1 if t == target else 0
            # 不能不选
            return sum(dfs(i - 1, t + j) for j in range(1, k + 1)) % MOD

        return dfs(n, 0)

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(n*target)  可以通过前缀和优化时间复杂度
        @space complexity:  O(n*target)  可以通过滚动数组优化空间复杂度
        @description:       翻译成递推即可
        """
        MOD = 10**9 + 7

        f = [[0] * (target + 1) for i in range(n + 1)]
        f[0][0] = 1

        for i in range(n):
            for j in range(1, target + 1):
                # 子问题 f[i][j] = f[i-1][x] (j-k <= x <= j-1)
                for x in range(max(0, j-k), j):
                    f[i + 1][j] += f[i][x]

        return f[n][target] % MOD
