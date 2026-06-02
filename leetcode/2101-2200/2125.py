"""
@title:      2125. 银行中的激光束数量
@difficulty: 简单
@importance: 2/5
@tags:       遍历
"""

from collections import Counter
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        @tags:              遍历即可
        @time complexity:   O(mn)
        @space complexity:  O(1)
        """
        pre = 0
        res = 0
        for i, v in enumerate(bank):
            c = v.count('1')
            if c != 0:
                if pre != 0:
                    res += pre * c
                pre = c
        return res
