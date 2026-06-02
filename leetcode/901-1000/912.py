"""
@title:      921. 使括号有效的最少添加
@difficulty: 简单
@importance: 4/5
@tags:       栈
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        @tags:              栈
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       括号匹配问题
        """
        stack = []
        for i in s:
            if stack and s == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
