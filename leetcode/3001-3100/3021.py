"""
@title:      3021. Alice 和 Bob 玩鲜花游戏
@difficulty: 中等
@importance: 3/5
@tags:       math 贪心
"""


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        @tags:              贪心
        @time complexity:   O(1)
        @space complexity:  O(1)
        @description:       题目的数据规模要求时间复杂度 < nlogn ，而遍历mn的时间复杂度为O(mn) ，所以一定存在O(1)的解法。
                            基数时 alice 获胜
        """
        # x在[1,n]区间取偶数 y在[1,m]区间取奇数
        a = (n // 2) * ((m // 2) + (m % 2))
        # x取奇数 y取偶数
        b = (m // 2) * ((n // 2) + (n % 2))
        return a + b
