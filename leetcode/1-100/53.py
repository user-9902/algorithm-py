"""
@title:      53. 最大子数组和
@difficulty: 简单
@importance: 5/5
@tags:       dp 分治 
"""
from typing import List
from functools import cache


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       f[i] = max(f[i-1] + nums[i], nums[i]) 。f[i]表示以i结尾的最大前缀和。由于连续性，nums[i]要么加入前缀和，要么单独组成子数组
        """
        n = len(nums)

        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = max(f[i-1] + nums[i], nums[i])
        return max(f)

    def maxSubArray(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       上一个解的空间优化。观察状态转移方程，不难发现 f[i] 只依赖于 f[i-1]
        """
        n = len(nums)
        pre = nums[0]
        ans = pre

        for i in range(1, n):
            pre = max(pre+nums[i], nums[i])
            ans = max(pre, ans)

        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        """
        分治
        """
        @cache
        def dfs(l, r):
            if l + 1 == r:
                return nums[l]
            m = (l+r) >> 1
            return max(dfs(l, m), dfs(m, r), dfs(l, m) + dfs(m, r))

        return dfs(0, len(nums))
