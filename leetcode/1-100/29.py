"""
@title:      29. 两数相除
@difficulty: 中等
@importance: 5/5
@tags:       二分 快速乘
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        @tags:              二分 快速乘
        @time complexity:   O(logn^2)
        @space complexity:  O(1)
        @description:       快速乘的实现同快速幂
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 边界条件处理
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX

        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        if dividend == 0:
            return 0

        negtive = (dividend > 0 and divisor < 0) or (
            dividend < 0 and divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        # 快速乘
        def quickAdd(a, b):
            res = 0
            add = a
            while b:
                if b & 1:
                    res += add
                add <<= 1
                b >>= 1
            return res

        left, right = 1, dividend
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            if quickAdd(mid, divisor) <= dividend:
                left = mid + 1
            else:
                right = mid - 1

        return -right if negtive else right
