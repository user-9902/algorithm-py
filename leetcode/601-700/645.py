"""
@title:      645. 错误的集合
@difficulty: 中等
@importance: 3/5
@tags:       sort math
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        @tags:              sort math
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       找到缺失的数通过set 再找出个正确错误数的差值即可得出结果
        """
        nums.sort()
        n = len(nums)
        b = 0
        for i in range(n):
            b += nums[i] - i - 1
        a = (n * (n + 1) // 2) - sum(set(nums))
        return [a + b, a]
