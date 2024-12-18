"""
@title:      283. 移动零
@difficulty: 简单
@importance: 5/5
@tags:       指针
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        @tags:              快慢指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        idx = 0
        for i, v in enumerate(nums):
            if v != 0:
                nums[idx] = v
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
