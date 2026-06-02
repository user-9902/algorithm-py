"""
name:       704. 二分查找
difficulty: 简单
importance: 5/5
tags:       binary_search
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        @tags:              binary_search
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       二分
        """
        # [left, right]
        l = 0
        r = len(nums) - 1
        # l=r时闭区间内任有元素继续
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:  # r 在该条件的限制下，最终会满足 nums[r] <= target
                r = mid - 1
            else:
                l = mid + 1

        return r if nums[r] == target else -1

    def search(self, nums: List[int], target: int) -> int:
        """
        @description:       左闭右开区间的写法
        """
        # target 落在 [left, right)区间中
        l = 0
        r = len(nums)
        # l=r时左闭右开区间内无元素
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < target: # 确保 nums[l] >= target
                l = mid + 1  # [mid+1, right)
            else:
                r = mid  # [l, mid)

        return l if nums[l] == target else -1

    def search(self, nums: List[int], target: int) -> int:
        """
        @description:      ❌ 左闭右开区间的错误写法 
        """
        # target 落在 [left, right)区间中
        l = 0
        r = len(nums)
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > target:
                l = mid   # [mid, right)
            else:
                # ❌ 可以发现 mid+1的比较被跳过了
                # 💲 写出区间的表示范围！！！就能发现错误
                r = mid + 1  # [l, mid+1)

        return l if nums[l] == target else -1


Solution().search([-1, 0, 3, 5, 9, 12], 9)
