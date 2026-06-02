"""
name:       75. 颜色分类 or 荷兰国旗问题
difficulty: 中等
importance: 5/5
tags:       快慢指针
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        @tags:              counter
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       记录每个颜色出现的次数，再次遍历数组重新填入数字即可
        """
        pass

    def sortColors(self, nums: List[int]) -> None:
        """
        @tags:              快慢指针 swap
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       从左向右遍历，如果遇到“红色0”则交换指针和下标i的数据，然后向右移动指针。再次处理“白色1”即可
        """
        n = len(nums)
        s = 0
        # 交换0
        for i in range(n):
            if nums[i] == 0:
                nums[s], nums[i] = nums[i], nums[s]
                s += 1
        # 交换1
        for i in range(s, n):
            if nums[i] == 1:
                nums[s], nums[i] = nums[i], nums[s]
                s += 1

    def sortColors(self, nums: List[int]) -> int:
        """
        @tags:              双指针 swap
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       一次遍历。上一解中是两次遍历 
        """
        n = len(nums)
        p1 = p2 = 0

        for i in range(0, n):
            # 1的处理同单指针一致
            if nums[i] == 1:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 += 1
            elif nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                # 特殊的点：0的移动可能会导致1被错误交换，1被错误交换了需要再换回来
                if p1 < p2:
                    nums[p2], nums[i] = nums[i], nums[p2]
                p1 += 1
                p2 += 1
