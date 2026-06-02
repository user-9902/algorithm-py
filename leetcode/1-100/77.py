"""
name:       77. 组合
difficulty: 中等
importance: 3/5
tags:       回溯
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        @tags:              回溯
        @time complexity:   O(n/k k)
        @space complexity:  O(k)
        """
        ans = []
        cur = []

        def dfs(idx, k):
            if k == 0:
                return ans.append(cur.copy())
            for i in range(idx, n + 1):
                cur.append(i)
                dfs(i + 1, k - 1)
                cur.pop()

        dfs(1, k)
        return ans
