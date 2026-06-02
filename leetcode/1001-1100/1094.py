"""
@title:      1094. 拼车
@difficulty: 简单
@importance: 5/5
@tags:       差分数组
"""

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        @tags:              差分数组
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       通过差分数组推出每个时间所需要的座位数，遍历需要的座位，判断是否能承载。
        """
        dif = [0] * 1001
        for num, f, t in trips:
            dif[f] += num
            dif[t] -= num
        for i, v in enumerate(dif):
            if i == 0:
                dif[i] = v
            else:
                dif[i] += dif[i-1]
        for v in dif:
            if v > capacity:
                return False
        return True
