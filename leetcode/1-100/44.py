"""
@title:      44. 通配符匹配
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        @tags:              dp
        @time complexity:   O(mn)
        @space complexity:  O(mn)
        @description:       分类讨论, 类似 leetcode 10,但好分析些 
        """
        n, m = len(s), len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True

        for i in range(m):
            if p[i] != "*":
                break
            f[0][i + 1] = True

        for i in range(n):
            for j in range(m):
                if p[j] == "*":
                    if f[i + 1][j]:  # *作为空字符串
                        f[i + 1][j + 1] = True
                    else:
                        for k in range(i + 1):  # 作为任意字符串
                            if f[k][j]:
                                f[i + 1][j + 1] = True
                                break
                elif p[j] == "?":
                    if f[i][j]:
                        f[i + 1][j + 1] = True
                else:
                    if f[i][j] and s[i] == p[j]:
                        f[i + 1][j + 1] = True
        return f[n][m]
