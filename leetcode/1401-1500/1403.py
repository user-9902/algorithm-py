"""
@title:      1403. 非递增顺序的最小子序列
@difficulty: 简单
@importance: 2/5
@tags:       sort
"""
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       排序即可
        """
        nums.sort(key=lambda x: -x)
        n = len(nums)
        sum_n = sum(nums)
        sum_r = 0
        for i in range(n):
            sum_r += nums[i]
            if 2 * sum_r > sum_n:
                return nums[:i+1]
