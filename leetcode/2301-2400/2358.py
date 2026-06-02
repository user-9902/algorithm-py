"""
@title:      2358. 分组的最大数量
@difficulty: 中等
@importance: 4/5
@tags:       sort 贪心 math
"""

from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        """
        @tags:              贪心 math
        @time complexity:   O(1)
        @space complexity:  O(1
        @description:       我们使第一个组是数字数量尽可能小，总和也经可能小
                            最佳的分组就是 1 2 3 4 5 ...
                            我们将数组中的元素排序 从小到达进行分组 分组按最佳分组来排序
                            (n * (n - 1)) / 2 <= len(grades)
                            解一元二次不等式即可
        """
        return int((-1 + (1 + 8 * len(grades)) ** 0.5) // 2)
