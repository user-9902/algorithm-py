"""
@title:      525. 连续数组
@difficulty: 简单
@importance: 4/5
@tags:       前缀和 hashmap
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        @tags:              前缀和 hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       前缀和差值 + hashmap的题已多次出现 参考leetcode560
        """
        map = {}
        map[0] = -1
        pre = 0  # 记录前缀1的个数
        ans = 0
        for i, v in enumerate(nums):
            if v == 1:
                pre += 1
            else:
                pre -= 1
            if pre in map:
                ans = max(ans, i - map[pre])
            else:
                map[pre] = i
        return ans
