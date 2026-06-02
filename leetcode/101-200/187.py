"""
@title:      187. 重复的DNA序列
@difficulty: 简单
@importance: 4/5
@tags:       hashmap
"""
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       统计子串出现的次数
        """
        n = len(s)
        m = {}
        for i in range(n-9):
            k = s[i:i+10]
            v = m.get(k, 0)
            m[k] = v + 1
        ans = []
        for k in m:
            if m[k] > 1:
                ans.append(k)
        return ans
