"""
@title:      1449. 数位成本和为目标值的最大数字
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from typing import List
from functools import cache


def help(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return s1
    elif n2 > n1:
        return s2
    for i in range(n1):
        if s1[i] > s2[i]:
            return s1
        elif s1[i] < s2[i]:
            return s2
    return s1


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """
        @tags:              递归
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       见下方解析
        """

        @cache
        def dfs(target):
            # 刚好花完target合法
            if target == 0:
                return ""

            # 默认是非法的
            res = "0"
            for i in range(9):
                if target >= cost[i]:
                    sub = dfs(target - cost[i])
                    if sub != "0":
                        # 字符串用数字的规则比大小，需要我们自己实现
                        res = help(res, str(i + 1) + sub)
            return res

        return dfs(target)

    def largestNumber(self, cost: List[int], target: int) -> str:
        """
        @tags:              递推
        @time complexity:   O(nm)
        @space complexity:  O(n)
        @description:       完全背包
        """
        f = [""] + ["0"] * target

        for i in range(9):
            for j in range(target + 1):
                if j >= cost[i] and f[j - cost[i]] != "0":
                    f[j] = help(f[j], str(i + 1) + f[j - cost[i]])
        return f[target]
