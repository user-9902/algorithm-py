"""
@title:      HJ22 汽水瓶
@difficulty: 简单
@importance: 4/5
@tags:       math 业务分析
"""


def cal(n):
    res = 0
    while n // 3:
        v = n // 3
        a = n % 3
        res += v
        n = v + a

    if n == 2:
        res += 1

    return res


while True:
    try:
        n = int(input())
        if n > 0:
            print(cal(n))
    except:
        break
