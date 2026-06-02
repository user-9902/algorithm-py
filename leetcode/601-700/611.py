"""
@title:      611. 有效三角形的个数
@difficulty: 中等
@importance: 3/5
@tags:       sort binary_search
"""

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        @tags:              sort binary_search
        @time complexity:   O(n^2logn)
        @space complexity:  O(1)
        @description:       遍历所有组合，第三个数的范围可以根据前两个数得出用二分优化
        """
        nums.sort()
        n = len(nums)
        res = 0

        for i in range(n-2):
            for j in range(i+1, n-1):
                target = nums[i] + nums[j]
                if nums[j+1] >= target:
                    continue
                l = j + 1
                r = n
                while l < r:
                    mid = (l + r) // 2
                    if nums[mid] < target:
                        l = mid + 1     # [mid+1, r)
                    else:
                        r = mid         # [l, mid)
                res += (r - j - 1)
        return res
