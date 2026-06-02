"""
@title:      1208. 尽可能使字符串相等
@difficulty: 简单
@importance: 4/5
@tags:       滑动窗口 前缀和
"""

import bisect


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        @tags:              前缀和 二分
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        """
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        ans = 0

        pre = [0] * (n+1)
        for i in range(1, n+1):
            pre[i] = pre[i-1] + cost[i-1]
        for i in range(1, n+1):
            v = pre[i]
            t = v - maxCost
            idx = bisect.bisect_left(pre, t)
            ans = max(i-idx, ans)
        return ans

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        @tags:              滑动窗口
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        n = len(s)
        l = 0
        sum_v = 0
        ans = 0
        for r in range(n):
            v = abs(ord(s[r]) - ord(t[r]))
            sum_v += v
            while sum_v > maxCost:
                sum_v -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            ans = max(r - l + 1, ans)
        return ans


Solution().equalSubstring("abcd", "bcdf", 3)
