"""
@title:      1262. 可被三整除的最大和
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List
from math import inf


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        @tags:              01背包
        @time complexity:   O(mn)
        @space complexity:  O(mn)
        @description:       f[i][j] 表示以 i 结尾余数为 j 的最大和。
                            f[i][j] = max(f[i-1], f[i-1][x] + nums[i]) 其中(nums[i] + x) % 3 = j
        """
        n = len(nums)
        f = [[-inf] * 3 for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(n):
            for j in range(3):
                # 不选    选
                # nums[i] % 3 == 0  x = 0
                # nums[i] % 3 == 1  x = 2
                # nums[i] % 3 == 0  x = j % 3
                f[i + 1][j] = max(f[i][j], f[i][(j + nums[i]) % 3] + nums[i])
        return f[n][0]


Solution().maxSumDivThree([3, 6, 5, 1, 8])
