"""
@title:      464. 我能赢吗
@difficulty: 中等
@importance: 4/5
@tags:       记忆化搜索
"""
from typing import List
from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        @tags:              递归 dfs
        @time complexity:   O(n^3)
        @space complexity:  O(n^3)
        @description:       将题目想象为一个三叉树的遍历, 加上一些剪枝即可。
        """
        if maxChoosableInteger > desiredTotal:
            return True
        if maxChoosableInteger / 2 * (2+(maxChoosableInteger - 1)) < desiredTotal:
            return False
        nums = [i for i in range(1, maxChoosableInteger)]

        @cache
        def dfs(step, pre):
            for i, v in enumerate(nums):
                if v == 0:
                    continue
                if pre + v >= desiredTotal:
                    return True
                nums[i] = 0
                if dfs(step+1, pre+v):
                    return False
        return dfs(0, 1)
