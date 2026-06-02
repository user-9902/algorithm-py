"""
@title:      67. 二进制求和
@difficulty: 简单
@importance: 5/5
@tags:       加法器 模拟
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        l = max(n, m)
        a = a.rjust(l, "0")
        b = b.rjust(l, "0")

        rest = False
        ans = ""
        for i in range(l - 1, -1, -1):
            cnt = 0
            if a[i] == "1":
                cnt += 1
            if b[i] == "1":
                cnt += 1
            if rest:
                cnt += 1
            ans = ("1" if cnt % 2 else "0") + ans
            rest = True if cnt > 1 else False
        return "1" + ans if rest else ans


Solution().addBinary("1010", "1011")
