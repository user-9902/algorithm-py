"""
@title:      646. 最长数对链
@difficulty: 中等
@importance: 4/5
@tags:       greedy dp sort
"""
from typing import List


class Solution:
    """
    同leetcode435
    """

    def findLongestChain(self, nums: List[List[int]]) -> int:
        """
        @tags:              sort dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       序列dp，f[i]表示以每个元素为数对链的最后一个元素能组成的最长长度
        """
        n = len(nums)
        nums.sort()

        f = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j][1] < nums[i][0]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)

    def findLongestChain(self, nums: List[List[int]]) -> int:
        """
        @tags:              sort greed
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       以结束位置进行排序, 从左向右遍历，能拼接的尽量拼接
        """
        n = len(nums)
        nums.sort(key=lambda x: x[1])

        right = nums[0][1]
        ans = 1
        for i in range(1, n):
            if nums[i][0] > right:
                ans += 1
                right = nums[i][1]
        return ans
