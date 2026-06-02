"""
@title:      1109. 航班预订统计
@difficulty: 简单
@importance: 4/5
@tags:       差分数组
"""

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        @tags:              差分数组 
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       直接运用差分数组即可
        """
        ans = [0] * (n + 1)
        for f, l, c in bookings:
            ans[f - 1] += c
            ans[l] -= c
        for i in range(1, n + 1):
            ans[i] += ans[i - 1]
        return ans[:-1]
