"""
@title:      494. 目标和
@difficulty: 中等
@importance: 5/5
@tags:       dp 01背包
"""

"""
假设 数组中分为两个部分的和 a 和 b
假设 a - b = target
假设 a + b = sum

推导：
a = target + b
target + b + b = sum
b = （target + sum） / 2

至此：
当数组中的一部分元素的和为 （target + sum） / 2 时，则有 a - b = target
即数组中挑出几个元素，使其和为 （target + sum） / 2 时，即满足题意
"""

from typing import List
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        @tags:              01背包
        @time complexity:   O(nm)
        @space complexity:  O(n)
        @desc:              f[i][j] = f[i-1][j] + f[i][j-k]
        """
        # new target
        t = target + sum(nums)
        # num 中元素都为正整数，下列情况无解
        if t < 0 or t % 2:
            return 0
        t >>= 1
        
        # 这里优化为一维数组
        f = [0]* (t + 1) # 防止越界加一
        f[0] = 1 # 初始状态

        for x in nums:
            for c in range(t, x-1, -1):
                    f[c] = f[c] + f[c-x]
        
        return f[t]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """
        递归
        """
        target += sum(nums)
        # num 都为正整数，下列情况无解
        if target < 0 or target % 2:
            return 0
        target >>= 1

        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i-1, c)
            # 选或者不选
            return dfs(i-1, c) + dfs(i-1, c - nums[i])

        return dfs(n-1, target)
