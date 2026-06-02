"""
name:       324. 摆动排序 II
difficulty: 
importance: 
tags:       sort
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        @tags:              sort swap
        @time complexity:   
        @space complexity:  
        @description:       
        @example:           112233  => 112 233 => 
        """
        n = len(nums)
        arr = sorted(nums)
        x = (n + 1) // 2
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1
