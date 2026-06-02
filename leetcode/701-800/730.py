"""
@title:      730. 统计不同回文子序列
@difficulty: 中等
@importance: 4/5
@tags:       
"""


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)

        f = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i][j] = 1 if j - i == 1 else 2 * f[i+1][j-1]
                else:
                    f[i][j] = f[i+1][j-1]
                if s[i+1] == s[j]:
                    f[i][j] += f[i+1][j]
                if s[i] == s[j-1]:
                    f[i][j] += f[i][j-1]

        return f[0][n - 1] % (10**9 + 7)


Solution().countPalindromicSubsequences("bccb")
