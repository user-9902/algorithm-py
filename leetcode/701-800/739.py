"""
@title:      739. 每日温度
@difficulty: 简单
@importance: 5/5
@tags:       单调栈
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        @tags:              单调栈
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       单调递减栈，栈里存的是下标
        """
        stack = []

        ans = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                pre = stack.pop()
                ans[pre[0]] = i - pre[0]
            stack.append([i, v])  # 这里没必要存二维数据，只需村下标即可，留作自我警示

        return ans


Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
