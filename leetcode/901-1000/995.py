"""
@title:      995. K 连续位的最小翻转次数
@difficulty: 困难
@importance: 4/5
@tags:       贪心 差分数组
"""

from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
        @tags:              贪心
        @time complexity:   O(nk)   ❌ 超时
        @space complexity:  O(1)
        @description:       这里的贪心策略就是从左至右，遇到0就反转。然后就能得出结果
        """
        def filp(idx):
            for i in range(k):
                nums[idx+i] = 1 if nums[idx+i] == 0 else 0

        n = len(nums)
        ans = 0
        for i in range(n-k+1):
            if nums[i] == 1:
                continue
            filp(i)
            ans += 1
        return ans if sum(nums) == n else -1

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
        @tags:              贪心
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       不去反转数组，而是利用差分数组记录当前反转次数，以优化时间复杂度
        """

        n = len(nums)
        diff = [0] * (n+1)
        ans = revCnt = 0
        for i in range(n):
            revCnt += diff[i]
            if (nums[i] + revCnt) % 2 == 0:
                if (i + k) > n:
                    return -1
                ans += 1
                revCnt += 1
                diff[i + k] -= 1
        return ans


Solution().minKBitFlips([0, 1, 0], 1)
