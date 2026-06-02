"""
@title:      209. 长度最小的子数组
@difficulty: 简单
@importance: 4/5
@tags:       滑动窗口 前缀和
"""
"""
💲
滑动窗口的题常常要求一个"满足条件"的"最优解"
移动右边界来"满足条件"
移动左边界来寻找"最优解"
"""




from typing import List
from math import inf
import bisect
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        @tags:              滑动窗口
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       移动右边界以满足窗口内的和>= target，移动左边界以寻找最小的长度
        """
        n = len(nums)
        l = r = 0
        tot = 0
        ans = n + 1
        while r < n:
            tot += nums[r]
            r += 1
            while tot >= target:
                ans = min(ans, r - l)
                tot -= nums[l]
                l += 1
        return 0 if ans == n + 1 else ans

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        @tags:              前缀和 binary search
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       
        """
        n = len(nums)
        # 得到前缀和数组
        for i in range(1, n):
            nums[i] += nums[i - 1]

        ans = inf
        for i in range(n):
            if nums[i] < target:
                continue
            t = nums[i] - target
            l = bisect.bisect_right(nums, t)
            ans = min(ans, i - l + 1)
        return 0 if ans == inf else ans
