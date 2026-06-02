"""
@title:      504. 七进制数
@difficulty: 简单
@importance: 5/5
@tags:       math
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        @tags:              10进制 -> n进制
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @desc:              💲进制转化
        """
        if num == 0:
            return "0"
        is_negative = num < 0
        num = abs(num)
        res = ""
        while num:
            res = str(num % 7) + res
            num //= 7
        return "-" + res if is_negative else res


def nine_to_ten_manual(nine_str):
    """
    @tags:              n进制 -> 10进制
    @time complexity:   O(logn)
    @space complexity:  O(1)
    """
    decimal_value = 0
    base = 9
    length = len(nine_str)

    for i in range(length):
        # 获取当前位的数字（从左至右）
        digit = int(nine_str[i])
        # 计算该位在10进制下的值并累加
        decimal_value += digit * (base ** (length - i - 1))
    return decimal_value
