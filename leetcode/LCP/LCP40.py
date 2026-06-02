"""
@title:      LCP 40. 心算挑战
@difficulty: 中等
@importance: 4/5
@tags:       greedy
"""

from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        n = len(cards)
        res = sum(cards[i] for i in range(n - 1, n - cnt - 1, -1))

        if res % 2 == 1:
            a = cards[-cnt]
            for i in range(n - cnt - 1, -1, -1):
                if cards[i] % 2 == a % 2:
                    i -= 1
                else:
                    res = res - a + cards[i]
                    break

        return 0 if res % 2 == 1 else res
