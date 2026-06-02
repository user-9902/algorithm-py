"""
@title:      22. 括号生成
@difficulty: 简单
@importance: 4/5
@tags:       dfs 回溯
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        @tags:              回溯 dfs
        @time complexity:   
        @space complexity:  
        @description:       枚举可能
        """
        ans = []
        s = ""

        def dfs(left, right):
            nonlocal s
            if left == n and right == n:
                ans.append(s)
            if left < n:
                s += "("
                dfs(left + 1, right)
                s = s[:-1]
            if right < left and right < n:
                s += ")"
                dfs(left, right + 1)
                s = s[:-1]

        dfs(0, 0)
        return ans
