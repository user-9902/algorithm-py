"""
@title:      57. 插入区间
@difficulty: 简单
@importance: 3/5
@tags:       sort
"""

from typing import List
import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        @tags:              二分 sort
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       先插入newinterval 然后就同leetcode 56
        """
        l = bisect.bisect_right(
            intervals, newInterval[0] - 1, key=lambda x: x[0])
        intervals.insert(l, newInterval)

        # 原数组上操作 减少复杂度
        cur = intervals[max(l - 1, 0)]
        i = max(l - 1, 0) + 1
        while i < len(intervals):
            if intervals[i][0] <= cur[1]:
                cur[1] = max(intervals[i][1], cur[1])
                intervals.pop(i)
            else:
                cur = intervals[i]
                i += 1
        return intervals
