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
        def dfs(i, pre):
            if i == n:
                return int(pre == target)
            return dfs(i + 1, pre + nums[i]) + dfs(i + 1, pre - nums[i])

        return dfs(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        @tags:              递归 dfs
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       01背包解的递归
        """
        t = sum(nums) + target
        # 无解
        if t % 2 or t < 0:
            return 0
        t >>= 1
        n = len(nums)

        @cache
        def dfs(i, t):
            if i < 0:
                return int(t == 0)
            if nums[i] > t:
                return dfs(i-1, t)
            else:
                return dfs(i-1, t - nums[i]) + dfs(i-1, t)

        return dfs(n-1, t)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       将上方01的思路翻译为dp
        """
        t = sum(nums) + target
        # 无解
        if t % 2 or t < 0:
            return 0
        t >>= 1
        n = len(nums)

        f = [[0] * (t + 1) for _ in range(n + 1)]
        # 从上一解递归中的边界条件得出这里的初始条件
        f[0][0] = 1
        for i in range(n):
            for j in range(t + 1):
                if j < nums[i]:
                    f[i + 1][j] = f[i][j]
                else:
                    f[i + 1][j] = f[i][j] + f[i][j - nums[i]]

        return f[n][t]


Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
