"""
@title:      952. 按公因数计算最大组件大小
@difficulty: 中等
@importance: 4/5
@tags:       并查集
"""

from typing import List
from math import gcd
from collections import Counter


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        """
        @tags:              并查集 公因数
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       
        """
        n = max(nums) + 1
        f = [i for i in range(n)]

        def father(x):
            res = f[x]
            if res != x:
                res = father(res)
                f[x] = res
            return res

        def union(x, y):
            fx, fy = father(x), father(y)
            if fx != fy:
                f[fx] = fy

        def search(x, y):
            return father(x) == father(y)

        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    union(i, num)
                    union(num // i, num)
                i += 1
        return max(Counter(father(i) for i in nums).values())


Solution().subArrayRanges([1, 2, 3])
