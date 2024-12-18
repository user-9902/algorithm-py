"""
@title:      15. 三数之和
@difficulty: 中等
@importance: 5/5
@tags:       sort 双指针
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        @tags:              快慢指针
        @time complexity:   O(n^2)
        @space complexity:  O(logN)
        @desc:              排序后，从左至右先敲定第一个数数字 a，双指针遍历余下两个数寻找 b + c = -a
        """
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n - 2):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    # 去重优化
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return ans
