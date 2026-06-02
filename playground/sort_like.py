"""
name:       类排序算法
difficulty: 中等
importance: 4/5
tags:       sort
"""
from typing import List
import random


class SortLike:
    def find_kth_smallest(self, nums: List[int], k: int):
        """
        @name:              寻找数组中排序为k的数
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       快排的思路，左右排序
        """
        def quick_sort(l, r, k):
            i = random.randint(l, r-1)
            nums[i], nums[l] = nums[l], nums[i]

            count = l
            for i in range(l+1, r):
                if nums[l] > nums[i]:
                    count += 1
                    nums[i], nums[count] = nums[count], nums[i]
            nums[l], nums[count] = nums[count], nums[l]

            if count == k:
                return nums[k]
            elif count > k:
                return quick_sort(l, count, k)
            else:
                return quick_sort(count + 1, r, k)

        return quick_sort(0, len(nums), k - 1)
