"""
@title:      523. 连续的子数组和
@difficulty: 中等
@importance: 4/5
@tags:       前缀和
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        @tags:              前缀和 fs
        @time complexity:   O(n^2)  ❌ 超时
        @space complexity:  O(n)
        @description:       求出前缀和，然后遍历前缀和差值
        """
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = nums[i - 1] + s[i - 1]
        for i in range(1, n):
            for j in range(i):
                v = s[i + 1] - s[j]
                if v % k == 0:
                    return True
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        @tags:              前缀和 hashmap math
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       同 leetcode 560 思路。(a % k + mod) - (b % k + mod) = 0 hashmap存储余数即可
        """
        n = len(nums)
        s = set()
        s.add(0)
        pre = 0
        for i in range(n):
            if i > 0:
                s.add((pre - nums[i-1]) % k)
                if (pre + nums[i]) % k in s:
                    return True
            pre += nums[i]
        return False


Solution().checkSubarraySum([2, 4, 3], 6)
