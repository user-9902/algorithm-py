"""
@title:      1004. 最大连续1的个数 III
@difficulty: 中等
@importance: 4/5
@tags:       滑动窗口 前缀和
"""

from typing import List
import bisect


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        @tags:              滑动窗口
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       窗口内的0的个数不能超过k，超过k则减小窗口，窗口每次改变都计算下最大长度
        """
        l = 0
        cnt = 0  # 统计区间内0的个数
        ans = 0
        for i, v in enumerate(nums):
            if v == 0:
                cnt += 1
            while cnt > k:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            ans = max(ans, i - l + 1)

        return ans

    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       统计0的个数，遍历前缀和差值求最大值。
        """
        n = len(nums)
        pre = [0] * n
        pre[0] = int(nums[0] == 0)
        for i in range(1, n):
            pre[i] = pre[i-1]
            if nums[i] == 0:
                pre[i] += 1

        ans = 0
        for i in range(n):
            if pre[i] <= k:
                ans = max(ans, i + 1)
            else:
                left = bisect.bisect_left(pre, pre[i] - k)
                ans = max(ans, i - left + 1)
        return ans
