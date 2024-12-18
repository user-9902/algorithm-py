"""
@title:      189. 轮转数组
@difficulty: 简单
@importance: 4/5
@tags:       数组 
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        @tags:              二倍数组
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       额外数组
        """
        n = len(nums)
        k %= n
        k = n - k
        res = nums + nums
        for i in range(k, k + n):
            nums[i - k] = res[i]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        @tags:              旋转
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       无额外数组
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
