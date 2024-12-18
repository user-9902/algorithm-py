"""
@title:      238. 除自身以外数组的乘积
@difficulty: 简单
@importance: 4/5
@tags:       前缀和
"""
from typing import List
import heapq


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       算出i位置的前缀乘积和后缀乘积。
        """
        n = len(nums)
        pre = [1] * n
        # 前缀积
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        # 后缀积
        post = [1] * n
        for i in range(n - 2, -1, -1):
            post[i] *= post[i + 1] * nums[i + 1]

        ans = [1] * n
        for i in range(n):
            ans[i] = pre[i] * post[i]
        return ans
