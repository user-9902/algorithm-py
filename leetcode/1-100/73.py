"""
@title:      73. 矩阵置零
@difficulty: 简单
@importance: 4/5
@tags:       数组 标签清除
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        @tags:              标记清除
        @time complexity:   O(n)
        @space complexity:  O(1)
        @desc:              第一行之外的元素，用第一行第一列来存储该行/列是否要清0。提前记录下第一行第一列本身是否有0
        """
        # 实现省略
