"""
@title:      303. 区域和检索 - 数组不可变
@difficulty: 简单
@importance: 4/5
@tags:       前缀和 设计题
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        """
        @tags:              前缀和
        @time complexity:   O(n*m)
        @space complexity:  O(n)    可改造原数组来优化
        @description:       前缀和  sum[left:right] == nums[right]的前缀和 - nums[left]的前缀和
        """
        n = len(nums)
        self.pre = [0] * (n + 1)
        for i in range(n):
            self.pre[i+1] = self.pre[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]
