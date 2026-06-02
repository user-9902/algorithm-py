"""
@title:      1074. 元素和为目标值的子矩阵数量
@difficulty: 中等
@importance: 5/5
@tags:       前缀和
"""

from typing import List
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(n*m^2)
        @space complexity:  O(n*m)
        @description:       
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] += matrix[i][j-1]
        ans = 0
        for i in range(n):
            pre = [0] * m
            for j in range(i, n):
                for k in range(m):
                    pre[k] += matrix[j][k]
                dic = defaultdict(int)
                dic[0] = 1
                for val in pre:
                    t = val - target
                    ans += dic[t]
                    dic[val] += 1
        return ans


Solution().numSubmatrixSumTarget([[1, -1], [-1, 1]], 0)
