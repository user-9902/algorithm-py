"""
@title:      1588. 所有奇数长度子数组的和
@difficulty: 简单
@importance: 4/5
@tags:       前缀和
"""

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        """
        n = len(arr)
        pre = [0] * (n+1)
        pre[0] = arr[0]
        for i in range(1, n+1):
            pre[i] = pre[i-1] + arr[i-1]

        ans = 0
        for i in range(n):
            for j in range(i, -1, -2):
                cur = pre[i+1] - pre[j]
                ans += cur
        return ans
