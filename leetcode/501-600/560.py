"""
@title:      560. 和为 K 的子数组
@difficulty: 中等
@importance: 5/5
@tags:       前缀和 hashmap
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        @tags:              前缀和 hasmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       寻求前缀和差值的过程 == 两数之和(leetcode1) 我们可以边遍历边用hashmap记录前缀和的值
        """
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = 0
        ans = 0
        for i, v in enumerate(nums):
            pre += v
            ans += cnt[pre - k]
            cnt[pre] += 1

        return ans
