"""
@title:      3208. 交替组 II
@difficulty: 中等
@importance: 5/5
@tags:       环状数组 取模
"""

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        @tags:              环状数组
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       遍历两倍长度，下标取模，这样就能统计环了。
        """
        n = len(colors)
        cnt = 1
        res = 0
        for i in range(1, 2 * n):
            if colors[i % n] != colors[(i - 1) % n]:
                cnt += 1
                # [0,n] 非环的部分去重
                if i >= n and cnt >= k:
                    res += 1
            else:
                cnt = 1
        return res


Solution().numberOfAlternatingGroups([0, 1, 0, 1, 0], 3)
