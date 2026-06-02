"""
@title:      1627. 带阈值的图连通性
@difficulty: 中等
@importance: 4/5
@tags:       并查集 公因数
"""
from typing import List


class Solution:
    def areConnected(
        self, n: int, threshold: int, queries: List[List[int]]
    ) -> List[bool]:
        """
        @tags:              并查集 公因数
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       同 leetcode 952
        """
        f = [i for i in range(n + 1)]

        def father(x):
            res = f[x]
            if res != x:
                res = father(res)
                f[x] = res
            return res

        def search(x, y):
            return father(x) == father(y)

        def merge(x, y):
            fx, fy = father(x), father(y)
            if fx != fy:
                f[fx] = fy

        for i in range(threshold + 1, n + 1):
            z = 1
            while z * z <= i:
                if i % z == 0:
                    if z > threshold:
                        merge(i, z)
                    if (i // z) > threshold:
                        merge(i, i // z)
                z += 1
        return [search(m, n) for m, n in queries]
