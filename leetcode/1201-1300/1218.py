"""
@title:      1218. 最长定差子序列
@difficulty: 简单
@importance: 4/5
@tags:       dp hashmap
"""
from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        @tags:              dp hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       两数之和的解题思路
        """
        n = len(arr)
        f = defaultdict(int)
        for i in range(n):
            f[arr[i]] = f[arr[i] - difference] + 1
        return max(f.values())
