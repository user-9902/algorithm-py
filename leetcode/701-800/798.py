"""
@title:      798. 得分最高的最小轮调
@difficulty: 困难
@importance: 4/5
@tags:       差分数组
"""

from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        """
        @tags:              差分数组 上下界分析
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:
        """
        n = len(nums)
        dif = [0] * (n+1)

        def add(l, r):
            dif[l] += 1
            dif[r] -= 1
        # 💲细心分析每一种情况
        for i, num in enumerate(nums):
            if num > i:
                add(i+1, i + 1 + n - num)
            elif num < i:
                add(0, i-num+1)
                add(i+1, n)
            elif num == i:
                add(0, 1)
                add(i+1, n)
        for i in range(1, n):
            dif[i] += dif[i-1]
        max_v = 0
        ans = 0
        for i in range(n):
            if dif[i] > max_v:
                max_v = dif[i]
                ans = i
        return ans
