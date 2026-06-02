"""
@title:      839. 相似字符串组
@difficulty: 中等
@importance: 4/5
@tags:       并查集
"""
from typing import List


class Solution:
    def build(self, n):
        self.f = [i for i in range(n)]
        self.cnt = n

    def father(self, idx):
        res = self.f[idx]
        if res != idx:
            res = self.father(res)
        return res

    def union(self, x, y):
        fx, fy = self.father(x), self.father(y)
        if fx != fy:
            self.f[fx] = fy
            self.cnt -= 1

    def is_similar_str(self, s1, s2):
        n = len(s1)
        s = 0
        for i in range(n):
            if s1[i] == s2[i]:
                s += 1
        return n - s <= 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        """
        @tags:              并查集
        @time complexity:   O(n*2)
        @space complexity:  O(n)
        @description:       并查集模板题
        """
        n = len(strs)
        self.build(n)

        for i in range(n):
            for j in range(i + 1, n):
                if self.is_similar_str(strs[i], strs[j]):
                    self.union(i, j)
        return self.cnt
