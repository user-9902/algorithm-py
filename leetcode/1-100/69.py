"""
@title:      69. x 的平方根 
@difficulty: 中等
@importance: 5/5
@tags:       二分 牛顿迭代
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        @tags:              二分
        @time complexity:   O(logx)   
        @space complexity:  O(1)
        """
        if x < 2:
            return x

        l = 2
        r = (x // 2) + 1
        while l < r:
            m = (l + r) // 2
            if m * m <= x:
                l = m + 1
            else:
                r = m
        return l - 1

    def mySqrt(self, x: int) -> int:
        """
        @tags:              牛顿迭代 数论
        @time complexity:   O(logx)   
        @space complexity:  O(1)
        """
        if x < 2:
            return x
        s = x
        def foo(x):
            res = (x + s / x) / 2
            # 找到结果 或到达精度极限
            if res == x:
                return x
            return foo(res)

        return int(foo(x))


Solution().mySqrt(4)
