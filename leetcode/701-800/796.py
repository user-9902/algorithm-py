"""
@title:      796. 旋转字符串
@difficulty: 简单
@importance: 4/5
@tags:       技巧 KMP
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        @tags:              math
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       若goal是s旋转得到，则goal一定是 s*2 的子串。
        @example:           s = 'abc'  goal = 'bca'  'bca' 是 'abcabc' 的子串。
        """
        n = len(s)
        if len(goal) != n:
            return False
        template = s * 2
        # 将题目转化为寻找子串的问题，可以再用 KMP 优化
        for i in range(n):
            if template[i:n+i] == goal:
                return True
        return False
