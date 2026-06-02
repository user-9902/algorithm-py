"""
@title:      1442. 形成两个异或相等数组的三元组数目
@difficulty: 简单
@importance: 3/5
@tags:       前缀和 位运算
"""

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        @tags:              前缀和 fs
        @time complexity:   O(n^2)  边遍历边计算可压缩至O(n)
        @space complexity:  O(n)
        @description:       前缀和的差值用以方便计算区间和，遍历每个奇数区间
        """
        n = len(arr)
        pre = [0] * (n+1)
        for i in range(1, n+1):
            pre[i] = pre[i-1] ^ arr[i-1]

        ans = 0
        for i in range(2, n+1):
            for j in range(i-1):
                if pre[i] == pre[j]:
                    ans += (i-j-1)
        return ans
