"""
@title:      765. 情侣牵手
@difficulty: 困难
@importance: 4/5
@tags:       并查集
"""

from typing import List


class Solution:
    def build(self, n):
        self.heads = [i for i in range(n)]
        self.set = n

    def find(self, i):
        idx = self.heads[i]
        if idx != i:
            idx = self.find(idx)
        return idx

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.heads[fx] = fy
            self.set -= 1

    def minSwapsCouples(self, row: List[int]) -> int:
        """
        @tags:              bfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       将问题化为子问题
                            01      坐序正确 无须交换
                            0213    两对坐序错误 需要一次交换
                            035241  三对坐序错误 需要两次交换
                            n对坐错  n对坐序错误 需要n-1次交换
                            因此我们要将坐序错误的情侣归入同一集合。
                            对于n对情侣 存在 k 个集合的情况,
        """
        n = len(row)
        self.build(n//2)
        for i in range(0, n, 2):
            self.union(row[i]//2, row[i+1]//2)
        return n // 2 - self.set


Solution().minSwapsCouples([5, 4, 2, 6, 3, 1, 0, 7])
