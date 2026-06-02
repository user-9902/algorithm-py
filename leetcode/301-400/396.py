"""
@title:      396. 旋转函数
@difficulty: 简单
@importance: 3/5
@tags:       math 前缀和
"""
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        @tags:              math
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       下一轮的值为可以由当前值计算而来：cur = cur + sum(nums) - 最后一个元素的值 * n
        """
        n = len(nums)
        cur = sum([i * nums[i] for i in range(n)])
        sum_n = sum(nums)

        ans = cur
        for i in range(n-1):
            cur += sum_n - n * nums[n-1-i]
            ans = max(ans, cur)
        return ans


Solution().maxRotateFunction([4, 3, 2, 6])
