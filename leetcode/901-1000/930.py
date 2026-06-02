"""
@title:      930. 和相同的二元子数组
@difficulty: 中等
@importance: 5/5
@tags:       前缀和 hashmap
"""

from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        @tags:              前缀和 hasmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       见 leetcode560
        """
        dic = defaultdict(int)
        dic[0] = 1
        pre = 0
        ans = 0
        for i in nums:
            pre += i
            t = pre - goal
            ans += dic[t]
            dic[pre] += 1
        return ans


Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2)
