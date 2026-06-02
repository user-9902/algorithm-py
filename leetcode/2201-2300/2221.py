"""
@title:      2221. 数组的三角和
@difficulty: 简单
@importance: 2/5
@tags:       模拟 数组
"""

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
        @tags:              模拟
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       模拟生成下一轮的数组
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            for j in range(i):
                nums[j] = nums[j] + nums[j+1]
        return nums[0] % 10
