"""
@title:      1751. 最多可以参加的会议数目 II
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""

"""
01背包
选或不选的问题
f[i][j] 表示枚举至第i个会议，至多参加j个会议的最大价值
f[i][j] = max(f[i-1][j], f[p][j-1] + value[i])
    f[i-1][j] 表示不选
    f[p][j-1] + value[i] 表示选
        其中p表示，选择i的时候，事件i能跟在事件p的后面
        为此需要将事件更具结束时间排序
最关键的就是在选当前会议的时候，如何去dp中寻找正确的值：
    会议i要能接上前面的会议，会议i的开始时间就必须比，前i-1内的事件的结束事件晚
    因此我们按照结束时间来遍历events，既先对events进行排序
"""




from typing import List
from bisect import bisect_left
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        @tags:              sort dp
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       01背包的变体 k表示背包容量
        """
        # 💲规划兼职，参加会议，单线程cpu等题中常见的排序技巧
        events.sort(key=lambda x: x[1])

        n = len(events)
        f = [[0] * (k + 1) for _ in range(n + 1)]

        for i, (start, end, val) in enumerate(events):
            # 当前选时 前面有多少会议   💲bisect_left 高级用法
            l = bisect_left(events, start, hi=i, key=lambda x: x[1])
            for j in range(1, k + 1):
                # 当前不选 当前选
                f[i + 1][j] = max(f[i][j], f[l][j - 1] + val)

        return f[n][k]
