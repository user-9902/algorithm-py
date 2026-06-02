"""
@title:      446. 等差数列划分 II - 子序列
@difficulty: 中等
@importance: 4/5
@tags:       dp 等差数列
"""
from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        @tags:              线性dp
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       遍历当前元素 i 前面的所有节点 j, 计算 i 与 j 的差值 gap
                                查询有多少公差为 gap ，结尾为 j 的数列。把 i 拼接入这些数列尾部，计入总的数列数量。
                                 i 和 j 两个元素单独组成新的公差为 gap 的数列。不计入总的数列数量，因为该新数列长度为 2。
        """
        n = len(nums)
        f = [defaultdict(int) for i in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                gap = nums[i] - nums[j]
                res += f[j][gap]
                # 拼在以 j 结尾的后面
                f[i][gap] += f[j][gap]
                # 与 j 单独组成
                f[i][gap] += 1
        return res
