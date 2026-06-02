"""
@title:      HJ21 简单密码
@difficulty: 简单
@importance: 3/5
@tags:       业务分析题
"""

import re

psw = input()
ans = ""
arr = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
for i in psw:
    v = i
    if re.search("[a-z]", v):
        for i, item in enumerate(arr):
            if v in item:
                v = str(i + 2)
    elif re.search("[A-Z]", v):
        if v == "Z":
            v = "a"
        else:
            v = chr(ord(v) + 33)    # 💲ord-chr的用法
    ans += v
print(ans)
