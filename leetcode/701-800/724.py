"""
@title:      724. 寻找数组的中心下标
@difficulty: 简单
@importance: 2/5
@tags:       前缀和
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        pre = 0
        sum_n = sum(nums)
        for i, v in enumerate(nums):
            if sum_n - v == 2 * pre:
                return i
            pre += v
        return -1
