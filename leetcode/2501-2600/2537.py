"""
@title:      2537. 统计好子数组的数目
@difficulty: 中等
@importance: 4/5
@tags:       滑动窗口 双指针
"""

from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        @tags:              滑动窗口 双指针
        @time complexity:   O(n)    数据规模决定了时间复杂度需要小于O(nlogn)
        @space complexity:  O(n)
        @desc:              遍历有边界，确认左边界。
        """
        n = len(nums)
        left = 0
        res = 0
        pairs = 0
        cnt = defaultdict(int)

        for right in range(n):
            # 增加右侧元素
            cnt[nums[right]] += 1
            if cnt[nums[right]] > 1:
                pairs += cnt[nums[right]] - 1

            # 当满足条件时，移动左侧指针以尝试缩小窗口
            while pairs >= k:
                res += (n - right)  # [l:r] 的子数组满足条件，更长的[l:k] (r<k<n) 子数组也能满足条件
                cnt[nums[left]] -= 1
                if cnt[nums[left]] >= 1:
                    pairs -= cnt[nums[left]]
                left += 1

        return res


print(Solution().countGood([1, 1, 1, 1, 1, 1, 7], 11))
