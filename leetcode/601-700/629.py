"""
@title:      629. K 个逆序对数组
@difficulty: 困难
@importance: 5/5
@tags:       dp 前缀和
"""


MOD = 10**9 + 7


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(n*m^2)  ❌超时
        @space complexity:  O(n*m)  
        @description:       f[i][j] 表示 n==i时 j==k时的方案数，f[i][j] = ∑ f[i-1][j-x] (0<=x<=i-1)
        """
        f = [[0] * (k+1) for _ in range(n+1)]
        f[0][0] = 1
        for i in range(1, n+1):
            for j in range(k+1):
                for x in range(j+1):
                    if x >= j-(i-1):
                        # f[i] 最多能为 f[i-1] 补充 i-1个值
                        f[i][j] += f[i-1][x] % MOD
        return f[n][k]

    def kInversePairs(self, n: int, k: int) -> int:
        """
        @tags:              dp + 前缀和
        @time complexity:   O(n*m)
        @space complexity:  O(n*m)  空间复杂度可以压缩为一维
        @description:       计算f[i][j]的循环部分可以通过 前缀和优化
        """
        f = [[0] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            pre = 0
            for j in range(k + 1):
                pre += f[i - 1][j]
                if j - (i - 1) > 0:
                    pre -= f[i - 1][j - (i - 1) - 1]
                f[i][j] = pre % MOD
        return f[n][k]
