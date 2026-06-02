"""
@title:      1035. 不相交的线
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(nm)
        @space complexity:  O(m)
        @description:       最公共子序列LCS模板题,见leetcode 1143
        """
        n, m = len(nums1), len(nums2)
        f = [0] * (m + 1)
        for i in range(n):
            pre = 0
            for j in range(m):
                tmp = f[j + 1]
                if nums1[i] == nums2[j]:
                    f[j + 1] = pre + 1
                else:
                    f[j + 1] = max(f[j + 1], f[j])
                pre = tmp
        return f[m]
