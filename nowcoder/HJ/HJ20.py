"""
@title:      HJ20 密码验证合格程序
@difficulty: 中等
@importance: 3/5
@tags:       业务分析题
"""

import re

"""
@tags:              业务分析
"""
res = [r"\d+", r"[a-z]", r"[A-Z]", r"[^a-zA-Z0-9]"]
while True:
    try:
        s = input()
        n = len(s)
        if n < 8:
            print("NG")
        elif sum([0 if re.search(i, s) is None else 1 for i in res]) < 3:
            print("NG")
        elif any([len(re.findall(s[i - 3: i], s)) > 1 for i in range(3, n)]):
            # s = '831(l)8^$O+3T' ❌ 这里会报错 💲不要使用字符串内容来正则匹配
            print("NG")
        else:
            print("OK")
    except:
        break


"""
@tags:              业务分析
"""
res = [r"\d+", r"[a-z]", r"[A-Z]", r"[^a-zA-Z0-9]"]


def foo(s):
    n = len(s)
    for i in range(3, n):
        t = s[i - 3: i]
        cnt = 0
        for j in range(3, n):
            if s[j - 3: j] == t:
                cnt += 1
        if cnt > 1:
            return False
    return True


while True:
    try:
        s = input()
        n = len(s)
        if n < 8:
            print("NG")
        elif sum([0 if re.search(i, s) is None else 1 for i in res]) < 3:
            print("NG")
        elif not foo(s):
            print("NG")
        else:
            print("OK")
    except:
        break
