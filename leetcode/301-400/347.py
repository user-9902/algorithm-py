"""
@title:      347. 前 K 个高频元素
@difficulty: 简单
@importance: 3/5
@tags:       堆 优先队列
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        @tags:              堆
        @time complexity:   O(n)   
        @space complexity:  O(n)
        @desc:              二分 第k大的数
        """
        # 实现省略