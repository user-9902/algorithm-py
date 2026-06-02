"""
@title:      1049. 最后一块石头的重量 II
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from functools import cache
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        @tags:              递归
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       01背包   题目难在如何将将题目转化为01背包，我们将石子分为两堆，左堆和右堆，sum(左) - sum(右) 越小越好。
                            题意就转化为使得选出数字之和最接近 sum(all) / 2
        """

        n = len(stones)
        sum_s = sum(stones)
        target = sum_s / 2

        @cache
        def dfs(i, target):
            if i < 0:
                return target

            return min(abs(dfs(i - 1, target)), abs(dfs(i - 1, target - stones[i])))

        return int(dfs(n - 1, target) * 2)
