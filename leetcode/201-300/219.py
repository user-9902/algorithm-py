"""
name:       219. 存在重复元素 II
difficulty: 简单
importance: 3/5
tags:       hashmap 滑动窗口
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       题目另一种表述，区间范围内是否存在重复的元素
        """
        hash_map = {}
        for i, v in enumerate(nums):
            if v in hash_map and i - hash_map[v] <= k:
                return True
            hash_map[v] = i
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        @tags:              滑动窗口
        @time complexity:   O(n)
        @space complexity:  O(k)
        @description:       滑动窗口
        """
        s = set()
        for i, v in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])   # 超出窗口限制
            if v in s:
                return True
            s.add(v)
        return False
