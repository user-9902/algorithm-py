"""
@title:      97. 交错字符串
@difficulty: 中等
@importance: 4/5
@tags:       记忆化搜索 dp
"""
from functools import cache


class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        @tags:              递归
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)
        @description:       判断s3的最后一个字符串是否来自s1或s2的最后一个字符串
                                来自s1则继续子问题 s3[:-1] 的最后一个字符串是否来自 s1[:-1] 或 s2
                                来自s2则继续子问题 s3[:-1] 的最后一个字符串是否来自 s1 或 s2[:-1]
        """
        n1, n2 = len(s1), len(s2)
        n = len(s3)

        if n != n1 + n2:
            return False

        if n1 == 0:
            return s3 == s2
        if n2 == 0:
            return s3 == s1

        return (
            s3[n - 1] == s1[n1 - 1] and self.isInterleave(s1[:-1], s2, s3[:-1])
        ) or (s3[n - 1] == s2[n2 - 1] and self.isInterleave(s1, s2[:-1], s3[:-1]))

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        @tags:              递归
        @time complexity:   O(n*m)
        @space complexity:  O(n*m)  可压缩至一维 状态依赖的是左、上相邻的值
        @description:       f[i][j] 表示 s1[i:] s2[j:] 能否组成 s3[i+j:]
        """
        n1, n2 = len(s1), len(s2)
        if len(s3) != n1 + n2:
            return False

        f = [[False] * (n2 + 1) for _ in range(n1 + 1)]

        # 边界条件处理
        f[0][0] = True
        for i in range(1, n1 + 1):
            f[i][0] = f[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n2 + 1):
            f[0][j] = f[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                f[i][j] = (f[i][j - 1] and s2[j-1] == s3[i + j - 1]) or \
                          (f[i - 1][j] and s1[i-1] == s3[i + j - 1])

        return f[n1][n2]
