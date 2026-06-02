"""
@title:      213. 打家劫舍 II
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)    
        @description:       环状的数据导致我们无法下手，找不到初始状态。这里我们人为创造初始状态，第一个元素选，第一个元素不选，然后就同打家劫舍I 
        """
        n = len(nums)

        if n < 3:
            return max(nums)

        # dp[0] 不选择第一家 dp[1] 选第一家
        dp = [nums[1], max(nums[1], nums[2])]
        for i in range(3, n):
            dp.append(max(dp[-2] + nums[i], dp[-1]))

        dp2 = [nums[0], nums[0]]
        for i in range(2, n-1):
            dp2.append(max(dp2[-2] + nums[i], dp2[-1]))

        return max(dp[-1], dp2[-1])


Solution().rob([1, 2, 1, 1])
