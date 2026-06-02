"""
@title:      1780. 判断一个数字是否可以表示成三的幂的和
@difficulty: 中等
@importance: 4/5
@tags:       进制转化 位运算 贪心
"""

from typing import List


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        @tags:              位运算
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       任何一个数都可以转化为3的幂的和，即转化为3进制数。
                            由于题意要求3的幂是互不相同的，因此将题意转化为判断3进制表示中每一位是否均 >=1。
        """
        while n:
            if n % 3 == 2:  # 余3，即获取3进制表示下的最低位
                return False
            n //= 3
        return True
