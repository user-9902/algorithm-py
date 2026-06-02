"""
@title:      2104. 子数组范围和
@difficulty: 中等
@importance: 4/5
@tags:       dp 单调栈
"""

from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        @tags:              dp fs
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       遍历所有子数组，计算最大值和最小值的差值即可。
        """
        n = len(nums)

        res = 0
        for i in range(n - 1, -1, -1):
            max_v = min_v = nums[i]
            for j in range(i + 1, n):
                max_v = max(max_v, nums[j])
                min_v = min(min_v, nums[j])
                res += max_v - min_v
        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       遍历所有子数组，计算最大值和最小值的差值即可。
        """
        n = len(nums)

        res = 0
        for i in range(n - 1, -1, -1):
            max_v = min_v = nums[i]
            for j in range(i + 1, n):
                max_v = max(max_v, nums[j])
                min_v = min(min_v, nums[j])
                res += max_v - min_v
        return res


Solution().subArrayRanges([1, 2, 3])
