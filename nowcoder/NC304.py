"""
@title:      NC304 最大子矩阵
@difficulty: 中等
@importance: 5/5
@tags:       前缀和
"""

from typing import List
from math import inf


class Solution:
    def getMaxMatrix(self, arr: List[List[int]]) -> int:
        """
        @tags:              二维最大子数组和
        @time complexity:   O(mn^2)
        @space complexity:  O(mn)
        @description:       二维最大子数组和 一维见 leetcode53
        """
        def help(f):
            n = len(f)
            pre = ans = f[0]
            for i in range(1, n):
                pre = max(pre + f[i], f[i])
                ans = max(ans, pre)
            return ans

        n, m = len(arr), len(arr[0])
        ans = -inf
        for i in range(n):
            f = [0] * m
            for j in range(i, n):
                for k in range(m):
                    f[k] += arr[j][k]
                ans = max(ans, help(f))
        return ans
