"""
@title:      403. 青蛙过河
@difficulty: 中等
@importance: 4/5
@tags:       记忆化搜索
"""
from typing import List
from functools import cache


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        @tags:              递归 dfs
        @time complexity:   O(n^3)
        @space complexity:  O(n^3)
        @description:       将题目想象为一个三叉树的遍历, 加上一些剪枝即可。
        """
        n = len(stones)
        s = set(stones)

        @cache
        def dfs(step, k):
            if k <= 0:
                return False
            cur = step + k
            if cur > stones[n - 1]:
                return False
            elif cur == stones[n - 1]:
                return True
            if cur in s:
                return dfs(cur, k - 1) or dfs(cur, k) or dfs(cur, k + 1)
            return False

        return dfs(0, 1)
