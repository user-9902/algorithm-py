"""
@title:      198. 打家劫舍
@difficulty: 中等
@importance: 5/5
@tags:       dp 
"""
from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        @tags:              递归
        @time complexity:   O(2^n)
        @space complexity:  O(n)    
        @description:       f(i) 求下标为i时的最大值。i可以选可以不选 不选就是f(i-1) 选则是num[i] + f(i-2)
        """
        @cache
        def f(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(f(i - 1), f(i - 2) + nums[i])    #

        n = len(nums)
        return f(n - 1)

    def rob(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)    f[i] 依赖于 f[i-1] f[i-2] 所以可优化至 O(1)
        @description:       当前这家可偷或不偷。f[i] = max(f[i-1], f[i-2] + nums[i])
        """
        n = len(nums)
        if n < 3:
            return max(nums)

        f = [0] * n
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(1, n):
            f[i] = max(f[i-1], f[i-2] + nums[i])
        return f[n-1]
