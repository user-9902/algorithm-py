"""
@title:      256. 粉刷房子 I
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        @tags:              路径dp
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       f[i][0] = min(f[i-1][1], f[i-1][2]) + costs[i][0]; f[i][1] f[i][2]同理
        """
        f = [[0, 0, 0] for _ in range(2)]

        for i in range(len(costs)):
            pre = (i - 1) % 2
            cur = i % 2
            f[cur][0] = min(f[pre][1], f[pre][2]) + costs[i][0]
            f[cur][1] = min(f[pre][0], f[pre][2]) + costs[i][1]
            f[cur][2] = min(f[pre][0], f[pre][1]) + costs[i][2]

        return min(f[(len(costs) - 1) % 2])
