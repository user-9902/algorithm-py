"""
@title:      1537. 最大得分
@difficulty: 中等
@importance: 4/5
@tags:       前缀和 
"""

from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(n+m)
        @space complexity:  O(n+m)
        @description:       根据相同的值将数组分段，计算每段的最大值
        """
        MOD = 10**9 + 7

        # 统计相同点
        n1, n2 = len(nums1), len(nums2)
        same1 = []
        same2 = []
        l1 = l2 = 0
        while l1 < n1 and l2 < n2:
            if nums1[l1] == nums2[l2]:
                same1.append(l1)
                same2.append(l2)
                l1 += 1
                l2 += 1
            elif nums1[l1] > nums2[l2]:
                l2 += 1
            else:
                l1 += 1

        if len(same1) == 0:
            return max(sum(nums1), sum(nums2))

        pre1 = [0] * (n1 + 1)
        for i in range(1, n1 + 1):
            pre1[i] = pre1[i - 1] + nums1[i - 1]

        pre2 = [0] * (n2 + 1)
        for i in range(1, n2 + 1):
            pre2[i] = pre2[i - 1] + nums2[i - 1]

        # 计算每一段的最大值
        ans = 0
        for i, v1 in enumerate(same1):
            v2 = same2[i]
            a = pre1[v1 + 1] - pre1[0 if i == 0 else same1[i - 1] + 1]
            b = pre2[v2 + 1] - pre2[0 if i == 0 else same2[i - 1] + 1]
            ans += max(a, b)
        ans += max(pre1[-1] - pre1[same1[-1] + 1],
                   pre2[-1] - pre2[same2[-1] + 1])
        return ans % MOD
