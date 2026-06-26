"""
@title:      304. 二维区域和检索 - 矩阵不可变
@difficulty: 中等
@importance: 4/5
@tags:       二维前缀和
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        @tags:              二维前缀和 
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       画个图观察便于理解 f[i][j] = f[i-1][j] + f[i][j-1] - f[i-1] + matrix[i][j]
        """
        n, m = len(matrix), len(matrix[0])
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = (
                    f[i + 1][j]
                    + f[i][j + 1]
                    - f[i][j]
                    + matrix[i][j]
                )

        self.n = n
        self.m = m
        self.f = f

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        @time complexity:   O(1)
        """
        return (
            self.f[row2 + 1][col2 + 1]
            - self.f[row1][col2 + 1]
            - self.f[row2 + 1][col1]
            + self.f[row1][col1]
        )
