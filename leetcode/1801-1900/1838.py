"""
@title:      1838. 最高频元素的频数
@difficulty: 中等
@importance: 4/5
@tags:       sort
"""
from typing import List
import heapq


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        @tags:              sort 暴力枚举
        @time complexity:   O(n^2)
        @space complexity:  O(logn)
        @description:       ❌ 超时
        """
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n - 1, -1, -1):
            l = i - 1
            cur = 0
            while l >= 0:
                if cur + nums[i] - nums[l] <= k:
                    cur += nums[i] - nums[l]
                    ans = max(i - l + 1, ans)
                    l -= 1
                else:
                    break
        return ans

    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        @tags:              sort 滑动窗口
        @time complexity:   O(n^2)
        @space complexity:  O(logn)
        @description:       计算窗口内的值是否满足k，不满足移动l，满足移动r以获得最大的r-l
        """
        n = len(nums)
        nums.sort()
        ans = 0

        l = r = 0
        cur_sum = 0
        while True:
            if (r - l) * nums[r] - cur_sum <= k:
                cur_sum += nums[r]
                r += 1
                ans = max(r - l, ans)
            else:
                cur_sum -= nums[l]
                l += 1
            if l == n or r == n:
                break
        return ans
