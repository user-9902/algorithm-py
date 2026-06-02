"""
@title:      345. 反转字符串中的元音字母
@difficulty: 简单
@importance: 3/5
@tags:       双指针
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        st = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        n = len(s)
        f = [False] * n
        for i, v in enumerate(s):
            if v in st:
                f[i] = True
        s2 = ''.join(s[i] if f[i] else '' for i in range(n))
        j = len(s2) - 1
        ans = ''
        for i in range(n):
            if f[i]:
                ans += s2[j]
                j -= 1
            else:
                ans += s[i]
        return ans


Solution().reverseVowels("leetcode")
