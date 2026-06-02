"""
name:       217. 存在重复元素 I
difficulty: 简单
importance: 3/5
tags:       hashmap sort
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(1)
        @description:       排序后，从前向后遍历，查看是否有重复元素
        """
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       遍历元素，元素在hashmap中存在return True，不存在就存入hashmap。
        """
        pass
