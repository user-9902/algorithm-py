"""
@title:      2300. 咒语和药水的成功对数
@difficulty: 简单
@importance: 4/5
@tags:       sort
"""
import bisect
import math
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """
        @tags:              binary_search sort
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       遍历即可
        """
        n, m = len(spells), len(potions)
        potions.sort()
        ans = [0] * n
        for i in range(n):
            target = math.ceil(success / spells[i])
            r = bisect.bisect_left(potions, target)
            ans[i] = m - r
        return ans
