"""
@title:      825. 适龄的朋友
@difficulty: 中等
@importance: 3/5
@tags:       排序 双指针
"""
from typing import List
from sortedcontainers import SortedList
import bisect


class KthLargest:

    def numFriendRequests(self, ages: List[int]) -> int:
        """
        @tags:              排序 双指针
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       从年龄低到高遍历数组，x能加到年龄的上下边界都随着x年龄的增加而增加。双指针确定能加到的年龄区间即可。
        """
        n = len(ages)
        ages.sort()
        res = 0
        slow = fast = 0
        for age in ages:
            if age < 15:
                continue
            # 能加到最小年龄的下标
            while ages[slow] <= 0.5 * age + 7:  # > 0.5 * age + 7
                slow += 1
            # 能加到最大年龄的下标
            while fast < n - 1 and ages[fast + 1] <= age:  # 💲推到第一个大于age的下标
                fast += 1
            res += fast - slow
        return res
