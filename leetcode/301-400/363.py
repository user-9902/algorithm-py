"""
@title:      363. 矩形区域不超过 K 的最大数值和
@difficulty: 困难
@importance: 5/5
@tags:       前缀和
"""
from typing import List
from sortedcontainers import SortedList
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        @tags:              前缀和 fs
        @time complexity:   O(n^2*m^2)  ❌超时
        @space complexity:  O(m*n)
        @description:       枚举点，一个矩形可以由左上角和右下角两个点确定，而枚举两个点的时间复杂度为 n^2*m^2
        """
        pass

    def maxSumSubmatrix(self, matrix: List[List[int]], target: int) -> int:
        """
        @tags:              前缀和 枚举三条边
        @time complexity:   O(n^2*m*logm)
        @space complexity:  O(m*n)
        @description:       枚举边
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] += matrix[i][j-1]

        ans = -float('inf')
        for i in range(n):
            help = [0] * m
            for j in range(i, n):
                sc = SortedList()
                # 枚举第三条边
                for k in range(m):
                    help[k] += matrix[j][k]
                    if help[k] <= target:
                        ans = max(ans, help[k])
                    if k > 0:
                        # help[k] - t <= target
                        t = help[k] - target
                        # 寻找 >= t的数
                        key = bisect.bisect_left(sc, t)
                        if key < len(sc):
                            ans = max(ans, help[k] - sc[key])
                    sc.add(help[k])
        return ans
