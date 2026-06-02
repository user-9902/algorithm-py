"""
@title:      1154. 一年中的第几天
@difficulty: 简单
@importance: 3/5
@tags:       计算
"""


M = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, 12):
    M[i] += M[i - 1]


def isLeapYear(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


class Solution:
    def dayOfYear(self, date: str) -> int:
        """
        @tags:              直接计算
        @time complexity:   O(1)
        @space complexity:  O(1)
        @description:       考虑闰月
        """
        y, m, d = list(map(int, date.split("-")))
        m = int(m)
        d = int(d)

        res = M[m - 1] + d
        if isLeapYear(y) and m > 2:
            res += 1
        return res


Solution().dayOfYear("2019-01-09")
