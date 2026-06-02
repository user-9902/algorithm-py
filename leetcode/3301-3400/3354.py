"""
@title:      3354. 使数组元素等于零
@difficulty: 中等
@importance: 3/5
@tags:       前缀和
"""

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       （题意难度中等）题意就是“打砖块“，在两个非0数间来回弹射。问能否清除所有”砖块“。
        """
        s = sum(nums)

        res = 0
        left = 0
        for i, v in enumerate(nums):
            if v != 0:
                left += v
                continue
            if abs(s - (2 * left)) == 1:
                res += 1
            elif s - (2 * left) == 0:
                res += 2
        return res
