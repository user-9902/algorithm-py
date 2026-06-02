"""
@title:      240. 搜索二维矩阵 II
@difficulty: 简单
@importance: 4/5
@tags:       二分
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        @tags:              二分
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       两次二分
        """
        n = len(matrix)
        m = len(matrix[0])

        # <= target的row
        l1 = 0
        r1 = n - 1
        while l1 <= r1:
            mid = (l1 + r1) // 2
            if matrix[mid][0] > target:
                r1 = mid - 1
            else:
                l1 = mid + 1

        for i in range(0, min(r1 + 1, n)):
            l2 = 0
            r2 = m - 1
            # 每行去求 <= target的值
            while l2 <= r2:
                mid = (l2 + r2) // 2
                if matrix[i][mid] > target:
                    r2 = mid - 1
                else:
                    l2 = mid + 1
            if matrix[i][r2] == target:
                return True

        return False
