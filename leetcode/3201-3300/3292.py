"""
@title:      3292. 形成目标字符串需要的最少字符串数 II
@difficulty: 困难
@importance: 5/5
@tags:       KMP dp
"""

from typing import List
from math import inf


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        """
        @tags:              KMP dp
        @time complexity:   O(k×(m+n))
        @space complexity:  O(m+n)
        """
        # 最长公共前后缀
        def kmp_next(s):
            n = len(s)
            nxt = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and s[i] != s[j]:
                    j = nxt[j - 1]
                if s[i] == s[j]:
                    j += 1
                nxt[i] = j
            return nxt

        n = len(target)

        back = [0] * n
        for word in words:
            m = len(word)
            nxt = kmp_next(word + "#" + target)
            for i in range(n):
                back[i] = max(back[i], nxt[i + m + 1])

        dp = [0] + [inf] * n
        for i in range(n):
            # i 结尾时的解
            dp[i + 1] = dp[i + 1 - back[i]] + 1
            if dp[i + 1] > n:
                return -1
        return dp[n]
