"""
@title:      875. 爱吃香蕉的珂珂
@difficulty: 中等
@importance: 4/5
@tags:       二分
"""
from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        @tags:              二分
        @time complexity:   O(nlogn)
        @space complexity:  O(1)
        @description:       已知k的最大值，最小值。求最小满足条件的值，二分寻找即可。
        """
        l = ceil(sum(piles) / h)
        r = max(piles)
        while l <= r:
            mid = l + ((r - l) >> 1)
            # k == mid的时候 吃完需要的时间
            time = sum([ceil(x / mid) for x in piles])
            # 保证 time <= h
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
