"""
@title:      923. 三数之和的多种可能
@difficulty: 中等
@importance: 5/5
@tags:       三数之和改
"""

from collections import Counter


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        cnt = Counter()
        for i in range(1, n+1):
            for j in range(n+1-i):
                cnt[s[j:j+i]] = i if cnt[s[j:j+i]] == 0 else 0
        return sum(cnt.values())


Solution().uniqueLetterString("ABA")
