"""
@title:      2055. 蜡烛之间的盘子
@difficulty: 中等
@importance: 4/5
@tags:       前缀和 二分
"""

from typing import List
import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        @tags:              前缀和 二分
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       计算蜡烛的前缀和，找到查询区间内的左右蜡烛，确认左右蜡烛区间内的蜡烛数量。
        """
        n = len(s)

        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + int(s[i - 1] == "|")
        for i, (l, r) in enumerate(queries):
            if pre[r + 1] - pre[l] < 2:
                queries[i] = 0
                continue
            left = bisect.bisect_left(pre, pre[l] + 1)
            right = bisect.bisect_left(pre, pre[r + 1])
            # 区间长度 - 区间内的蜡烛数量
            queries[i] = right - left + 1 - (pre[r + 1] - pre[l])
        return queries


Solution().platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]])
