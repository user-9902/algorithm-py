"""
@title:      74. 搜索二维矩阵
@difficulty: 简单
@importance: 3/5
@tags:       二分
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        @tags:              两次二分
        @time complexity:   O(logn)
        @space complexity:  O(1)
        """
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = n
        while l < r:
            mid = (l + r) >> 1
            if matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid

        if l < n and matrix[l][0] == target:
            return True

        a = 0
        b = m
        while a < b:
            mid = (a + b) >> 1
            if matrix[l - 1][mid] < target:
                a = mid + 1
            else:
                b = mid
        return a < m and matrix[l - 1][a] == target
