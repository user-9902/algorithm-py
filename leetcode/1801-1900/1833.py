"""
@title:      1833. 雪糕的最大数量
@difficulty: 简单
@importance: 5/5
@tags:       计数排序
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        @tags:              计数排序
        @time complexity:   O(n)    n = max_val - min_val
        @space complexity:  O(n)
        @description:       计数排序
        """
        max_v = max(costs)
        min_v = min(costs)
        f = [0] * (max_v - min_v + 1)
        for i in costs:
            f[i - min_v] += 1
        res = []
        for i, v in enumerate(f):
            while v > 0:
                res.append(i+min_v)
                v -= 1
        ans = 0
        for i in res:
            if coins >= i:
                coins -= i
                ans += 1
            else:
                break
        return ans


Solution().maxIceCream([1, 3, 2, 4, 1], 7)
