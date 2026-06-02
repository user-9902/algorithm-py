"""
@title:      HJ17 坐标移动
@difficulty: 简单
@importance: 3/5
@tags:       业务分析题
"""
directives = input().split(";")


def isLegal(s: str) -> bool:
    n = len(s)
    if n > 3 or n < 2:
        return False
    if not s[0] in ["A", "D", "W", "S"]:
        return False
    return s[1:].isdigit()


a = b = 0
for i, v in enumerate(directives):
    if isLegal(v):
        step = int(v[1:])
        match v[0]:
            case 'A':
                a -= step
            case 'D':
                a += step
            case 'W':
                b += step
            case 'S':
                b -= step
print('{},{}'.format(a, b)) # 💲py模板字符串
