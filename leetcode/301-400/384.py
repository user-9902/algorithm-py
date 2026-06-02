"""
@title:      384. 打乱数组
@difficulty: 中等
@importance: 5/5
@tags:       随机抽样 洗牌算法
"""


from typing import List
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @tags:              💲洗牌算法 Fisher-Yates
    @time complexity:   init: O(n)  reset:O(n) shuffle: O(n)
    @space complexity:  init: O(n)  reset:O(n) shuffle: O(1)
    @description:       洗牌算法，遍历每个元素i，从 [i,n)中随机选取元素替换
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.org = nums[::]

    def reset(self) -> List[int]:
        self.nums = self.org[::]
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = random.randrange(i, n)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


Solution([1, 2, 3, 4, 5]).shuffle()
