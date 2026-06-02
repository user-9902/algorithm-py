"""
@title:      583. 两个字符串的删除操作
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        """
        @tags:              LCS
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)
        @description:       最长公共子序列变体
        """
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                f[i+1][j+1] = f[i][j] + 1 if word1[i] == word2[j] else max(f[i+1][j], f[i][j+1])
        
        return m + n - 2 * f[n][m]
