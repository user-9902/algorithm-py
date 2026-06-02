"""
@title:      886. 可能的二分法
@difficulty: 中等
@importance: 5/5
@tags:       并查集
"""


from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        @tags:              并查集
        @time complexity:   O(n+m)   
        @space complexity:  O(n)
        @description:       反向集合 + 并查集
        """
        # 创造集合 和 反向集合 f[i] 表示集合i  f[i + n] 表示不包含i的集合
        f = [i for i in range((n + 1) * 2)]

        def father(x):
            if f[x] != x:
                f[x] = father(f[x])
            return f[x]

        def query(x, y):
            return father(x) == father(y)

        def union(x, y):
            fx, fy = father(x), father(y)
            if fx != fy:
                f[fx] = fy

        for a, b in dislikes:
            # a，b出现在同一集合
            if query(a, b):
                return False
            # 集合 a 和不包含 b的集合合并
            union(a, b + n)
            # 集合 b 和不包含 a的集合合并
            union(a + n, b)
        return True
