"""
@title:      522. 最长特殊序列 II
@difficulty: 中等
@importance: 3/5
@tags:       fs sort
"""

from typing import List
from functools import cache


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        @tags:              sort fs
        @time complexity:   O(n^2m)
        @space complexity:  O(n^2m)
        @description:       遍历所有可能，找到无子序列的字符串的最大值。排序优化：从更长的字符串开始遍历，满足题意就可以返回了
        """
        # s是否是t的子序列
        def is_subseq(s, t):
            n = len(s)
            idx = 0
            for c in t:
                if c == s[idx]:
                    idx += 1
                    if idx == n:
                        return True
            return False

        strs.sort(key=lambda x: -len(x))
        for i, s in enumerate(strs):
            if all(i == j or not is_subseq(s, t) for j, t in enumerate(strs)):
                return len(s)
        return -1


Solution().findLUSlength(["aba", "cdc", "eae"])
