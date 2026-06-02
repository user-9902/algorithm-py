"""
@title:      746. 使用最小花费爬楼梯
@difficulty: 简单
@importance: 5/5
@tags:       dp
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        @tags:              dp 斐波那契数列
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       先写出迭代公式 c[n] = min(c[n-1], c[n-2]) + cost[i]
        """
        # 注意可以 "跨上" 最后一级台阶，也可以 "跨过" 最后一级台阶
        cost.append(0)
        n = len(cost)
        f = [0] * n
        f[0] = cost[0]
        f[1] = cost[1]
        for i in range(2, n):
            f[i] = min(f[i - 1], f[i - 2]) + cost[i]
        return f[n-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        @tags:              dp + 状态压缩
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        n = len(cost)
        a = cost[0]
        b = cost[1]
        for i in range(2, n):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)
