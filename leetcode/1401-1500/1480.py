"""
@title:      1480. 一维数组的动态和
@difficulty: 简单
@importance: 1/5
@tags:       前缀和
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        return nums
