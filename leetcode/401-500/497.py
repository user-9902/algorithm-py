"""
@title:      497. 非重叠矩形中的随机点
@difficulty: 简单
@importance: 4/5
@tags:       随机抽样
"""

from typing import List
from random import randint
import bisect


class Solution:
    """
    @tags:              前缀和 随机抽样
    @description:       随机抽样的题目，要保证等概率要求。
    """

    def __init__(self, rects: List[List[int]]):
        n = len(rects)
        areas = [0] * n
        for i, v in enumerate(rects):
            areas[i] = (v[2] - v[0] + 1) * (v[3] - v[1] + 1)  # 边上的值也算在内
            if i > 0:
                areas[i] += areas[i - 1]
        self.rects = rects
        self.areas = areas
        self.sums = areas[n - 1]

    def pick(self) -> List[int]:
        # 💲randint(a,b)  范围在[a,b]闭区间内的值
        res = randint(1, self.sums)
        k = bisect.bisect_left(self.areas, res)
        point = self.rects[k]
        return [randint(point[0], point[2]), randint(point[1], point[3])]


Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]).pick()
