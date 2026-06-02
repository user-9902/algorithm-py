"""
@title:      664. 奇怪的打印机
@difficulty: 困难
@importance: 4/5
@tags:       dp
"""
from math import inf


class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        @tags:              区间dp
        @time complexity:   O(n^3)
        @space complexity:  O(n^2)
        @description:       见注释 思路困难
        """
        n = len(s)
        f = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            f[i][i] = 1
            for j in range(i+1, n):
                # s[j] == s[i] 时 s[j]可以和s[i]一起被打印，f[i][j] = f[i][j-1]
                if s[i] == s[j]:
                    f[i][j] = f[i][j-1]
                else:
                    # s[j] 和 s[i] 无法一起被打印，考虑将f[j]归入哪个区间的打印
                    f[i][j] = inf
                    for k in range(i, j):
                        f[i][j] = min(f[i][j], f[i][k] + f[k+1][j])
        return f[0][n-1]
