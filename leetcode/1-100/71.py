"""
name:       71. 简化路径
difficulty: 中等
importance: 4/5
tags:       stack 业务分析
"""

import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        @tags:              stack 
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       维护路径栈
        """
        p = re.split("/+", path)
        stack = []
        for i in p:
            if i == "." or i == "":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)
