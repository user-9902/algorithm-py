"""
@title:      781. 森林中的兔子
@difficulty: 中等
@importance: 3/5
@tags:       math greedy
"""

from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        @tags:              math
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       当有 k+1 只值为 k 的兔子时，这k+1只兔子颜色相同
        """
        count = Counter(answers)
        res = 0
        for k in count:
            v = count[k]
            res += (v // (k + 1)) * (k+1)
            if res % (k + 1):
                res += k + 1
        return res


Solution().numRabbits([1, 1, 2])
