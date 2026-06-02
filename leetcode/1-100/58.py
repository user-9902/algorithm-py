"""
@title:      58. 最后一个单词的长度
@difficulty: 简单
@importance: 5/5
@tags:       双指针
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        @tags:              双指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       注意边界条件的分析
        """
        n = len(s)
        r = n
        for i in range(n - 1, -1, -1):
            # 几下第一个非空串下标
            if s[i] != " ":
                if r == n:
                    r = i
            # 第二次遇到非空串
            else:
                if r < n:
                    return r - i
        # 遇不到第二次非空串
        return r + 1


Solution().lengthOfLastWord("Hello World")
