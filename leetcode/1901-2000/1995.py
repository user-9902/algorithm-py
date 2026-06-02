"""
@title:      1995. 统计特殊四元组
@difficulty: 中等
@importance: 4/5
@tags:       hasmap dp
"""
from typing import List
from collections import Counter


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        @tags:              hash
        @time complexity:   O(n^3)
        @space complexity:  O(n^3)  
        @description:       遍历三个数 + 两数之和hashmap解
        """
        n = len(nums)
        ans = 0
        for t in range(3, n):
            for i in range(0, t-2):
                target = nums[t] - nums[i]
                cnt = Counter()
                for k in range(i+1, t):
                    ans += cnt[target - nums[k]]
                    cnt[nums[k]] += 1
        return ans

    def countQuadruplets(self, nums: List[int]) -> int:
        """
        @tags:              hash
        @time complexity:   O(n^3)
        @space complexity:  O(n^3)  
        @description:       多维01背包
        """
        n = len(nums)
        max_v = max(nums)

        f = [[[0] * 4 for _ in range(max_v+1)] for i in range(n + 1)]
        f[0][0][0] = 1
        for i in range(n):
            f[i][0][0] = 1
            for j in range(max_v+1):
                for k in range(1, 4):
                    f[i + 1][j][k] = f[i][j][k]
                    if j >= nums[i]:
                        f[i + 1][j][k] += f[i][j - nums[i]][k - 1]

        return sum(f[i][nums[i]][3] for i in range(3, n))
