"""
@title:      638. 大礼包
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from functools import cache
from typing import List
from math import inf


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        """
        @tags:              递归
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)
        @description:       多维度完全背包
        """
        # 删除无优惠的礼包
        n = len(special)
        m = len(price)
        for i in range(n - 1, -1, -1):
            if special[i][m] > sum(special[i][j] * price[j] for j in range(m)):
                special.pop(i)

        @cache
        def dfs(i, *needs):
            if i < 0:
                res = 0
                for k in range(m):
                    if needs[k] < 0:
                        res += inf
                    else:
                        res += needs[k] * price[k]
                return res
            if any(special[i][j] > needs[j] for j in range(len(needs))):
                return dfs(i - 1, *needs)
            else:
                needs2 = [needs[j] - special[i][j] for j in range(len(needs))]
                return min(dfs(i - 1, *needs), dfs(i, *needs2) + special[i][-1])

        return dfs(len(special) - 1, *needs)
