"""
@title:      152. 乘积最大子数组
@difficulty: 中等
@importance: 5/5
@tags:       sort
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       整体思路可参考leetcode53。这里需要多考虑负数的情况，因为最大值可能在正负之间转化。因此我们同时记录下最大 最小值。
        """
        n = len(nums)
        f1 = nums.copy()
        f2 = nums.copy()
        for i in range(1, n):
            v = nums[i]
            f1[i] = max(f1[i-1]*v, f2[i-1]*v, v)    # leetcode53 的状态方程为：f[i] = max(f[i-1], v) 这里需要我们考虑正负转化的情况。
            f2[i] = min(f1[i-1]*v, f2[i-1]*v, v)
        return max(f1)


Solution().maxProduct([2, 3, -2, 4])
