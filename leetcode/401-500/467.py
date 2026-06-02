"""
@title:      467. 环绕字符串中唯一的子字符串
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""

from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        """
        @tags:              线性dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        """
        f = defaultdict(int)
        k = 0
        for i, ch in enumerate(s):
            # 当前字符能否和前面的字符组成子串
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                k += 1
            else:
                k = 1
            # 记录当前字符能组成的最长连续子串的长度。如：abcd 只需记录长度 4,表示存在子串 d cd bcd abcd
            f[ch] = max(f[ch], k)
        return sum(f.values())
