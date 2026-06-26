"""
@title:      204. 计数质数
@difficulty: 中等
@importance: 5/5
@tags:       math
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        """
        @tags:              math
        @time complexity:   
        @space complexity:  O(1)
        @description:       记住质数的一个性质即可：大于2，3的质数，一定可以写成 6^x+1 or 6^x-1
                            枚举上面的这些数，然后判断是否是素数即可。
        """
        # 实现省略