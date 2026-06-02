"""
@title:      526. 优美的排列
@difficulty: 简单
@importance: 5/5
@tags:       dp 状态压缩 位运算
"""

from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        """
        @tags:              递推 位运算优化 
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       枚举当前数的可能性来实现，用位运算来压缩存储的状态。
        """
        statue = (1 << n) - 1

        @cache
        def dfs(s: int):
            # 所有数都用上 1111
            if s == statue:
                return 1
            else:
                res = 0
                # 当前选第几个数
                i = s.bit_count() + 1
                for j in range(1, n + 1):
                    # j 还未被使用 and 满足题目的计算条件
                    if s >> (j - 1) & 1 == 0 and (j % i == 0 or i % j == 0):
                        res += dfs(s | (1 << j - 1))
                return res

        return dfs(0)

    def countArrangement(self, n: int) -> int:
        """
        @tags:              递推 
        @time complexity:   O(n2^n)
        @space complexity:  O(2^n)
        @description:       f[i] 表示 
        """
        u = (1 << n) - 1
        f = [0] * (u + 1)
        f[0] = 1
        for s in range(1, u + 1):
            i = s.bit_count()
            for j in range(1, n + 1):
                # s 用上了 j 且 j 满足计算条件
                if s >> (j - 1) & 1 and (j % i == 0 or i % j == 0):
                    # j 之外的数
                    f[s] += f[s ^ (1 << (j - 1))]
        return f[u]


Solution().countArrangement(4)
