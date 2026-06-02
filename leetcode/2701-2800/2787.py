"""
@title:      2787. 将一个数字表示成幂的和的方案数
@difficulty: 中等
@importance: 3/5
@tags:       dp 01背包
"""

"""
直接的01背包题
可选元素为 [1, pow(n, 1/x)]
背包大小为 n
"""


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """
        @tags:              01背包
        @time complexity:   O(n pow(n,1/x))   
        @space complexity:  O(n^2) 可优化为一维数组
        """
        # 01背包 背包规模为n 可选项为1-k (k**x <= n)
        MOD = 10 ** 9 + 7
        f = [[0] * (n+1) for _ in range(n+1)]
        f[0][0] = 1

        for i in range(1, n+1):
            v = i ** x
            for j in range(n+1):
                # 选不了
                if v > j:
                    f[i][j] = f[i-1][j]
                else:
                    f[i][j] = (f[i-1][j] + f[i-1][j - v]) % MOD
        return f[n][n]
