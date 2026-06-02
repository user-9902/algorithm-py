"""
@title:      1310. 子数组异或查询
@difficulty: 简单
@importance: 3/5
@tags:       位运算
"""

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        @tags:              前缀和 二分
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       a xor 0 = a; a xor a = 0;
        """
        n = len(arr)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] ^ arr[i - 1]
        return [pre[r + 1] ^ pre[l] for l, r in queries]
