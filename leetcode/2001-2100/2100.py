"""
@title:      2100. 适合野炊的日子
@difficulty: 中等
@importance: 4/5
@tags:       预处理
"""

from typing import List
import bisect


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """
        @tags:              预处理 
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       按题意递增 递减性处理数组
        """
        n = len(security)
        pre = [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                pre[i] = pre[i-1] + 1
        post = [0] * n
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                post[i] = post[i+1] + 1
        ans = []
        for i in range(time, n-time):
            if post[i] >= time and pre[i] >= time:
                ans.append(i)
        return ans
