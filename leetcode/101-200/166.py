"""
@title:      166. 分数到小数
@difficulty: 中等
@importance: 5/5
@tags:       长除法 math 业务分析
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        @tags:              顺序比较
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       长除法 余数*10 
        """
        minus = (numerator < 0 and denominator > 0) or (
            numerator > 0 and denominator < 0
        )
        numerator = abs(numerator)
        denominator = abs(denominator)
        # 整数部分
        a = numerator // denominator
        numerator %= denominator
        # 小数部分
        b = []
        m = {}
        idx = 0
        denominator = abs(denominator)
        left = None
        while True:
            if numerator == 0:
                break
            numerator *= 10
            if numerator in m:
                left = m[numerator]
                break
            m[numerator] = idx

            cur = numerator // denominator
            numerator %= denominator
            b.append(cur)
            idx += 1

        if left is not None:
            ans = (
                str(a)
                + "."
                + "".join(str(b[i]) for i in range(0, left))
                + "("
                + "".join(str(b[i]) for i in range(left, len(b)))
                + ")"
            )
        else:
            ans = str(a)
            if len(b):
                ans += "." + "".join(str(i) for i in b)
        return "-" + ans if minus else ans
