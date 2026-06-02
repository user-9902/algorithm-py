"""
@title:      241. 为运算表达式设计优先级
@difficulty: 中等
@importance: 5/5
@tags:       分治
"""

from typing import List
import re
from functools import cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        @tags:              dfs 分治
        @time complexity:   O(2^n) n为数字的个数
        @space complexity:  O(n)
        @description:       按照运算符将原问题切割为左右两个部分，再合并计算
        """
        s = re.findall('\d+|\+|-|\*', expression)

        @cache
        def dfs(l, r):
            if r-l == 1:
                return [int(s[l])]
            res = []
            for i in range(l+1, r, 2):
                left = dfs(l, i)
                right = dfs(i+1, r)
                # merge
                for x in left:
                    for y in right:
                        if s[i] == '*':
                            res.append(x * y)
                        if s[i] == '-':
                            res.append(x - y)
                        if s[i] == '+':
                            res.append(x + y)
            return res
        return dfs(0, len(s))


Solution().diffWaysToCompute("2*3-4*5")
