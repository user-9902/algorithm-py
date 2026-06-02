"""
@title:      239. 滑动窗口最大值
@difficulty: 中等
@importance: 4/5
@tags:       滑动窗口 优先队列
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        @tags:              滑动窗口
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       维护一个大根堆即可，参考堆排序。
        """
        # 实现省略