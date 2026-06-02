"""
@title:      1749. 任意子数组和的绝对值的最大值
@difficulty: 中等   
@importance: 4/5
@tags:       前缀和 dp
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        @tags:              前缀和 sort
        @time complexity:   O(0)
        @space complexity:  O(0)
        """
        sl = SortedList()
        pre = 0
        res = 0
        for i in nums:
            sl.add(pre)
            pre += i
            res = max(res, abs(pre - sl[0]), abs(pre - sl[-1]))
        return res

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(0)
        @space complexity:  O(0)
        @description:       同leetcode53
        """
        n = len(nums)
        fmin = 0
        fmax = 0
        ans = 0
        for i in nums:
            fmin = min(fmin + i, i)
            fmax = max(fmax + i, i)
            ans = max(ans, abs(fmax), abs(fmin))
        return ans


Solution().maxAbsoluteSum([1, -3, 2, 3, -4])
