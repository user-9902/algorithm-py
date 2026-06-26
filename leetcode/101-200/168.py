"""
@title:      168. Excel表列名称
@difficulty: 中等
@importance: 5/5
@tags:       math 余数运算
"""


class Solution:
    def convertToTitle(self, num: int) -> str:
        """
        @tags:              26进制
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       长除法 余数*10 
        """
        # 26 进制
        ans = ''
        a_i = ord("A")
        while num > 0:
            num -= 1 # 这里的26位从1开始，因此需要-1
            cur = num % 26
            ans = chr(a_i + cur) + ans
            num //= 26
        return ans


Solution().convertToTitle(701)
print(ord("A"))
