"""
@title:      1879. 两个数组最小的异或值之和
@difficulty: 中等
@importance: 4/5
@tags:       状压dp
"""
from functools import cache
from typing import List
from math import inf


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        @tags:              dp 状态压缩
        @time complexity:   O(n*m)   
        @space complexity:  O(m)
        @description:       fs 的解 → dp优化重复计算 → 状态压缩
        """
        n, m = len(nums1), len(nums2)

        @cache
        def dfs(i, u):
            if i == -1:
                return 0
            res = inf
            for j in range(m):
                if (1 << j) & u:
                    res = min(res, (nums1[i] ^ nums2[j]) +
                              dfs(i - 1, u ^ (1 << j)))
            return res

        return dfs(n - 1, (1 << m) - 1)
