"""
@title:      51. N 皇后 I
@difficulty: 中等
@importance: 5/5
@tags:       回溯算法
"""
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        """
        @tags:              dfs 回溯算法 math
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       枚举所有排列组合的可能，确保枚举的可能不破坏规则。枚举行上的可能，确保同一列上无重复，同一斜线上无重复。
        """
        f = ["." * n] * n
        # 列上是否已经有Q
        col = [False] * n
        # 正斜边上是否已经有Q 斜线上是否重复用截距计算
        deg = [False] * 2 * n
        # 负斜边上是否已经有Q
        udeg = [False] * 2 * n

        ans = []

        def dfs(i):
            if i == n:
                return

            for j in range(n):
                if col[j] or deg[n - i + j] or udeg[i + j]:
                    continue
                f[i] = f[i][:j] + "Q" + f[i][j + 1:]
                if i == n - 1:
                    ans.append(f[::])
                col[j] = udeg[i + j] = deg[n - i + j] = True
                dfs(i + 1)
                # 状态回溯
                col[j] = udeg[i + j] = deg[n - i + j] = False
                f[i] = "." * n

        dfs(0)
        return ans


Solution().totalNQueens
