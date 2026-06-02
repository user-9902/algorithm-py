"""
@title:      581. 最短无序连续子数组
@difficulty: 简单
@importance: 3/5
@tags:       sort
"""

from math import inf
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        @tags:              sort              
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       排序完，双指针寻找乱序部分
        """
        arr = sorted(nums)
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            if nums[l] == arr[l]:
                l += 1
            else:
                break
        if l == r:
            return 0

        while l < r:
            if nums[r] == arr[r]:
                r -= 1
            else:
                break
        return r - l + 1


Solution().findUnsortedSubarray([1, 2, 3, 4])
