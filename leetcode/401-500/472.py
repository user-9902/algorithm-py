"""
@title:      472. 连接词
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        @tags:              序列dp
        @time complexity:   O(n*m^2)   
        @space complexity:  O(n*m)
        @description:       能否拼接的思路见leetcode 139
        """
        ans = []
        s = set(words)
        for idx, item in enumerate(words):
            m = len(item)
            f = [False] * (m+1)
            f[0] = True
            for x in range(m):
                for y in range(x+1):
                    if f[y] and item[y:x+1] in s and item[y:x+1] != item:
                        f[x+1] = True
                        break
            if f[m]:
                ans.append(item)
        return ans
