"""
@title:      48. 旋转图像
@difficulty: 简单
@importance: 4/5
@tags:       模拟
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        @tags:              模拟
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       原地旋转
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n - i - 1):
                (
                    matrix[i][j],
                    matrix[j][n - i - 1],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[n - 1 - j][i],
                ) = (
                    matrix[n - 1 - j][i],
                    matrix[i][j],
                    matrix[j][n - i - 1],
                    matrix[n - 1 - i][n - 1 - j],
                )
