"""
@title:      72. 编辑距离
@difficulty: 中等
@importance: 6/5
@tags:       LPS dp
"""
from functools import cache
from math import inf


class Solution:
    """
    word1 -> word2 等价于 word2 -> word1
    对word1的插入，删除，替换 -> 等价于word1插入，word2插入，word1或word2替换

    dp[i][j] 表示为 word1第i位之前的字符，转为word2第j位之前的字符所需的最小操作步骤
    word[i] = word[j]: dp[i][j] = dp[i-1][j-1]
    word[i] != word[j]: dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
    """

    def minDistance(self, word1: str, word2: str) -> int:
        """
        @tags:              递归
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)
        """
        n, m = len(word1), len(word2)

        @cache
        def dfs(i, j):
            # 边界条件。word1为空字符串，那么需要插入 j+1 个字符串变成 word2
            if i < 0:
                return j + 1
            elif j < 0:
                return i + 1
            # 两种情况
            elif word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            else:
                return min(dfs(i - 1, j - 1), dfs(i, j - 1), dfs(i - 1, j)) + 1

        return dfs(n - 1, m - 1)

    def minDistance(self, word1: str, word2: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)  可以压缩至一维，观察状态方程，f[i][j] 依赖的是相邻的上、左、左上三个状态
        @description:       递归翻译成递推
        """
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n+1):
            f[i][0] = i
        for i in range(m+1):
            f[0][i] = i
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    f[i + 1][j + 1] = f[i][j]
                else:
                    # 三种情况，word1插入 word2插入 word1替换
                    f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1], f[i][j]) + 1
        return f[n][m]
