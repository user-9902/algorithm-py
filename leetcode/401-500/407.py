"""
@title:      407. 接雨水 II
@difficulty: 中等
@importance: 4/5
@tags:       单调栈
"""
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        @tags:              dp 单调栈
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       同leetcode42

        """
        n, m = len(heightMap), len(heightMap[0])
        # 左侧最值
        left = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(1, m):
                left[i][j] = max(left[i][j - 1], heightMap[i][j - 1])

        # 右
        right = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m - 2, -1, -1):
                right[i][j] = max(right[i][j + 1], heightMap[i][j + 1])

        # 上
        top = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(m):
                top[i][j] = max(top[i - 1][j], heightMap[i - 1][j])

        # 下
        bottom = [[0] * m for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(m):
                bottom[i][j] = max(bottom[i + 1][j], heightMap[i + 1][j])

        ans = 0
        for i in range(n):
            for j in range(m):
                a = (
                    min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                    - heightMap[i][j]
                )
                if a > 0:
                    ans += a
        return ans
