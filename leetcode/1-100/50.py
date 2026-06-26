"""
@title:      50. Pow(x, n)
@difficulty: 简单
@importance: 5/5
@tags:       快速幂 二进制
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        @tags:              快速幂
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       如 x^19 = x * x^2 * x^16
        """
        ans = 1
        if n < 0:  # 处理负数 x^-n = (1/x)^n
            n = -n
            x = 1 / x
        while n:
            if n & 1: # n视为二进制 100101
                ans *= x  # 把 x^n 乘到 ans 中
            x *= x
            n >>= 1
        return ans
