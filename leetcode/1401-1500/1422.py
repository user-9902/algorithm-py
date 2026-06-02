"""
@title:      1422. 分割字符串的最大得分
@difficulty: 简单
@importance: 2/5
@tags:       前缀和
"""

from typing import List


class Solution:
    def maxScore(self, s: str) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(n)
        """
        n = len(s)
        pre = [0] * n
        pre[0] = int(s[0] == "1")
        for i in range(1, n):
            pre[i] = pre[i - 1] + int(s[i] == "1")
        ans = 0
        for i in range(n - 1):
            ans = max(ans, i+1 - pre[i] + pre[n-1] - pre[i])
        return ans
