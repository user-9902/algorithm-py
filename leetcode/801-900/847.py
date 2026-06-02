"""
@title:      847. 访问所有节点的最短路径
@difficulty: 困难
@importance: 4/5
@tags:       dp 状态压缩 位运算
"""

from functools import cache
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        @tags:              递推 位运算优化 
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       枚举当前数的可能性来实现，用位运算来压缩存储的状态。
        """
