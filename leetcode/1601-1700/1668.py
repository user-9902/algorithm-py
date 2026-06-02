"""
@title:      1668. 最大重复子字符串
@difficulty: 中等   题目存在fs的解所以是简单题
@importance: 4/5
@tags:       dp
"""

from typing import List


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(mn)
        @space complexity:  O(n)
        @description:       线性dp
        """
        n, m = len(sequence), len(word)
        f = [0] * (n+1)
        for i in range(m-1, n+1):
            if word == sequence[i-m:i]:
                f[i] = f[i-m] + 1
        return max(f)
