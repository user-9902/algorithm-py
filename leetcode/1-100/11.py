"""
@title:      11. 盛最多水的容器
@difficulty: 中等
@importance: 5/5
@tags:       双指针 贪心
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        @tags:              双指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @desc:              指针置于左右两端，每次移动高度短指针，因为宽度一定是在递减的，高度要尽可能的高，移动短板。
                            贪心的题更多的是记忆，一时难相同，证明也困难。
        """
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[r], height[l]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return ans
