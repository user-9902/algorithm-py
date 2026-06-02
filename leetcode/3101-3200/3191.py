"""
@title:      3191. 使二进制数组全部等于 1 的最少操作次数 I
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            if nums[i] == 0:
                ans += 1
                for j in range(i, i+3):
                    nums[j] = 1 if nums[j] == 0 else 0
        return ans if nums[n - 1] == 1 and nums[n - 2] == 1 else -1

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            if nums[i] == 0:
                ans += 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        return ans if nums[n - 1] == 1 and nums[n - 2] == 1 else -1


Solution().minOperations([0, 1, 1, 1, 0, 0])
