"""
@title:      52. N 皇后 II
@difficulty: 中等
@importance: 0/5    同 leetcode 51
@tags:       回溯算法
"""
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        @tags:              dfs 回溯算法 math
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       枚举所有排列组合的可能，确保枚举的可能不破坏规则。枚举行上的可能，确保同一列上无重复，同一斜线上无重复。
        """
        # 列上是否已经有Q
        col = [False] * n
        # 正斜边上是否已经有Q 斜线上是否重复用截距计算
        deg = [False] * 2 * n
        # 负斜边上是否已经有Q
        udeg = [False] * 2 * n

        ans = 0

        def dfs(i):
            nonlocal ans

            if i == n:
                return

            for j in range(n):
                if col[j] or udeg[n - i + j] or deg[i + j]:
                    continue
                if i == n - 1:
                    ans += 1

                col[j] = True
                # 斜率1 -i = j + b
                deg[i + j] = True
                # 斜率-1
                udeg[n - i + j] = True
                dfs(i + 1)
                # 状态回溯
                col[j] = False
                deg[i + j] = False
                udeg[n - i + j] = False

        dfs(0)
        return ans
