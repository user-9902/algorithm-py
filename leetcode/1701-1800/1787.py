"""
@title:      1787. 使所有区间的异或结果为零
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""


from typing import List
from bisect import bisect_left


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len()
