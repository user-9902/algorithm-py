"""
@title:      3542. 将所有元素变为 0 的最少操作次数
@difficulty: 中等
@importance: 5/5
@tags:       单调栈
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        @tags:              单调栈
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       
        """
        stack = [0]
        n = len(nums)
        ans = 0
        for i in range(n):
            v = nums[i]
            if v < stack[-1]:
                while len(stack) and v < stack[-1]:
                    ans += 1
                    stack.pop()
            if v > stack[-1]:
                stack.append(v)
        return ans + len(stack) - 1


Solution().minOperations([3, 1, 2, 1])
