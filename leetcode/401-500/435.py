"""
@title:      435. 无重叠区间
@difficulty: 中等
@importance: 5/5
@tags:       dp greedy
"""
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       dp的思路同最长递增子序列（leetcode300）
        """
        nums.sort()
        n = len(nums)
        f = [1] * n

        # python 会超时
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i][0] >= nums[j][1]:
        #             f[i] = max(f[i], f[j] + 1)
        # return n - max(f)

        # 可以通过迭代器优化
        for i in range(n):
            f[i] = max((f[j] for j in range(i) if nums[i]
                       [0] >= nums[j][1]), default=0) + 1
        return n - max(f)

    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        """
        @tags:              greedy
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       尽可能留足空间，我们后续才可能加入更多的切片。为确保右侧留足空间，依照nums[1]的大小对数组进行排序。然后从左到右开始遍历，能插入的片段就插入，因为右侧空间更足。
        """
        n = len(nums)
        nums.sort(key=lambda x: x[1])

        right = nums[0][1]
        ans = 1
        for i in range(1, n):
            if nums[i][0] >= right:
                ans += 1
                right = nums[i][1]
        return n - ans
