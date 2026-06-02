"""
@title:      394. 字符串解码
@difficulty: 简单
@importance: 4/5
@tags:       dfs 栈 业务模拟
"""

import re


class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(leng, s):
            num_len = 0
            left = None
            n = 0
            res = ""
            for i, c in enumerate(s):
                if c == "[":
                    if n == 0:
                        left = i
                    n += 1
                elif c == "]":
                    n -= 1
                    if n == 0:
                        res += dfs(int(s[left - num_len: left]),
                                   s[left + 1: i])
                        num_len = 0
                elif re.match(r"[a-z]", c) and n == 0:
                    res += c
                elif re.match(r"[0-9]", c) and n == 0:
                    num_len += 1
            return leng * res
        return dfs(1, s)


Solution().decodeString("3[a]2[bc]")
