"""
@title:      207. 课程表
@difficulty: 简单
@importance: 5/5
@tags:       拓扑排序 Kahn
"""

from typing import List


class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        @tags:              拓扑排序
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       同 leetcode 210
        """
        # 省略实现