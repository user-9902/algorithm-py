"""
@title:      1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
@difficulty: 中等
@importance: 4/5
@tags:       业务分析 前缀和
"""

from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       计算到第i天最多最少能吃多少糖果，判断能否吃到目标糖果
        """
        n = len(candiesCount)
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] + candiesCount[i - 1]
        for i, (t, d, c) in enumerate(queries):
            mi = d
            ma = (d + 1) * c
            queries[i] = pre[t] + candiesCount[t] > mi and pre[t] < ma
        return queries
