"""
@title:      42. 接雨水
@difficulty: 中等
@importance: 5/5
@tags:       单调栈 双指针
"""
from typing import List


class Solution:
    """
    每个块能装的雨水由最大前缀和最大后缀中的小者决定
    """

    def trap(self, height: List[int]) -> int:
        """
        @tags:              dp 单调栈
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       算出最大前后缀然后，然后计算每个块能装的雨水
                            cur = min(max_left, max_right) - cur_height
                            左右边界的实现实例和列求解一样，只要存储左边界即可，求有边界的时候同时求解即可。
        """
        n = len(height)
        pre = [0] * n   # 用以记录前缀最大值
        for i in range(1, n):
            pre[i] = max(pre[i - 1], height[i - 1])

        post = 0    # 用以记录后缀最大值 减少一边遍历边计算后缀和边计算结果
        res = 0
        for i in range(n - 2, -1, -1):
            post = max(post, height[i + 1])
            a = min(post, pre[i]) - height[i]
            if a > 0:
                res += a
        return res

    def trap2(self, height: List[int]) -> int:
        """
        @tags:              双指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       前后缀最大值在计算的时候都是递增的，前后缀其中小者，决定了其相邻元素能接多少水，移动小者。
        """
        n = len(height)
        pre_max = height[0]
        post_max = height[n - 1]
        l = 1
        r = n - 2

        res = 0
        while l <= r:
            if pre_max < post_max:
                a = pre_max - height[l]
                if a > 0:
                    res += a
                pre_max = max(pre_max, height[l])
                l += 1
            else:
                a = post_max - height[r]
                if a > 0:
                    res += a
                post_max = max(post_max, height[r])
                r -= 1
        return res
