"""
@title:      153. 寻找旋转排序数组中的最小值
@difficulty: 中等
@importance: 4/5
@tags:       二分
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        @tags:              二分
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       和最后一个元素比较，
        """
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[n - 1]:
                l = mid + 1  # [mid+1, r)
            else:
                r = mid  # [l,mid)
        return nums[l]
