"""
@title:      374. 猜数字大小
@difficulty: 简单
@importance: 5/5
@tags:       二分
"""
import random


def guess():
    return random.randint(-1, 1)


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        @tags:              二分
        @time complexity:   O(logn)   
        @space complexity:  O(1)
        """
        l = 1
        r = n + 1
        while l < r:
            mid = (l + r) >> 1  # (l + (r - l)) >> 1
            if guess(mid) <= 0:
                r = mid  # [l, mid)
            else:
                l = mid + 1  # [mid+1, r)
        return l
