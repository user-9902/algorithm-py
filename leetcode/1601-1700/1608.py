"""
@title:      1608. 特殊数组的特征值
@difficulty: 简单
@importance: 2/5
@tags:       sort
"""
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       排序即可
        """
        nums.sort()
        n = len(nums)
        for i in range(n):
            l = 0
            r = n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < n - i:
                    l = mid + 1
                else:
                    r = mid
            if n - l == n - i:
                return n - i
        return -1
