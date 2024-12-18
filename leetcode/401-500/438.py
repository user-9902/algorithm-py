"""
name:       438. 找到字符串中所有字母异位词
difficulty: 简单
importance: 4/5
tags:       滑动窗口
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        @tags:              滑动窗口
        @time complexity:   O(m+(n−m)×Σ)
        @space complexity:  O(Σ)
        @description:       s窗口内的字符的数量和p的字符数量相同。
        """
        n = len(p)

        u = ord("a")
        p_c = [0] * 26
        for c in p:
            p_c[ord(c) - u] += 1

        ans = []
        l = 0
        for i, c in enumerate(s):
            p_c[ord(c) - u] -= 1
            if i - l == n:
                p_c[ord(s[l]) - u] += 1
                l += 1
            if all(i == 0 for i in p_c):
                ans.append(i - n + 1)
        return ans
