"""
@title:      1450. 在既定时间做作业的学生人数
@difficulty: 简单
@importance: 4/5
@tags:       差分数组
"""

from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
        @tags:              差分数组
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       直接运用差分数组即可
        """
        f = [0] * 10001
        n = len(startTime)
        for i in range(n):
            f[startTime[i]] += 1
            f[endTime[i] + 1] -= 1
        for i in range(1, len(f)):
            f[i] += f[i - 1]
        return f[queryTime]
