"""
@title:      528. 按权重随机选择
@difficulty: 简单
@importance: 4/5
@tags:       随机抽样
"""

from typing import List
import random
import bisect


class Solution:
    """
    @tags:              前缀和 随机抽样
    """

    def __init__(self, w: List[int]):
        n = len(w)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = w[i] + s[i]
        self.s = s

    def pickIndex(self) -> int:
        random_v = random.randint(1, self.s[-1])
        return bisect.bisect_left(self.s, random_v) - 1
