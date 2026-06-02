"""
@title:      190. 颠倒二进制位
@difficulty: 简单
@importance: 5/5
@tags:       位运算
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        @tags:              位运算
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       长除法 余数*10 
        """
        res = 0
        for _ in range(32):
            res <<= 1
            res |= n & 1
            n >>= 1
        return res
