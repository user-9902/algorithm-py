"""
@title:      3255. 长度为 K 的子数组的能量值 II
@difficulty: 简单
@importance: 4/5
@tags:       前缀预处理
"""

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """ 
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       预处理，判断以每个元素结尾时，连续且上升的值。
        """
        n = len(nums)
        f = [1] * n
        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                f[i] = f[i-1] + 1
        res = [-1] * (n - k + 1)
        for i in range(k-1, n):
            if f[i] >= k:
                res[i-k+1] = nums[i]
        return res
