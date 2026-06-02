"""
@title:      45. 跳跃游戏 II
@difficulty: 简单
@importance: 4/5
@tags:       贪心
"""

from typing import List
from functools import cache


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        @tags:              fs
        @time complexity:   O(n^n)  ❌ 时间复杂度超了。💲复杂度分析很重要
        @space complexity:  O(1)
        """
        n = len(nums)
        if n < 2:
            return 0

        @cache
        def dfs(i, step):
            if i >= n - 1:
                return step

            res = n + 1
            for j in range(1, nums[i] + 1):
                res = min(res, dfs(i + j, step + 1))
            return res

        return dfs(0, 0)

    def jump(self, nums: List[int]) -> int:
        """
        @tags:              贪心
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        n = len(nums)

        r = 0       # 每轮的右边界
        mail = 0    # 最远能到达的距离
        ans = 0
        for i in range(n-1):
            mail = max(mail, i+nums[i])
            # 进入下一轮
            if i == r:
                ans += 1
                r = mail  # 下一轮的最远距离，便是下一轮的右边界
        return ans
