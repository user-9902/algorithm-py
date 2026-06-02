"""
@title:      27. 移除元素
@difficulty: 简单
@importance: 5/5
@tags:       指针
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        @tags:              cnt
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       记录结果下标即可
        """
        s = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[s], nums[i] = nums[i], nums[s]
                s += 1
        return s
