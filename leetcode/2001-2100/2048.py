"""
@title:      2048. 下一个更大的数值平衡数
@difficulty: 中等
@importance: 3/5
@tags:       枚举
"""

from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        """
        @tags:              暴力枚举
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       枚举大于n的数字，判断是否满足题意，受数据规模限制，能满足题意
        """
        while True:
            n += 1
            cnt = Counter(str(n))
            if all(int(d) == c for d, c in cnt.items()):
                return n
