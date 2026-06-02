"""
@title:      HJ18 坐标移动
@difficulty: 中等
@importance: 3/5
@tags:       业务分析题 较繁杂 💲要耐心读完题，耐心！
"""


def isLegal(item):
    try:
        a = [int(i) for i in item[0]]
        b = [int(i) for i in item[1]]
        # 校验ip是否合法
        if a[0] == 127 or a[0] == 0:
            return None
        for i in a:
            if i > 256 or i < 0:
                return False
        # 校验掩码是否合法
        l = 0
        r = 3
        while b[l] == 255:
            l += 1
        while b[r] == 0:
            r -= 1
        if l == 4 or r == -1 or l < r:
            return False
        if l == r and (not b[r] in [254, 252, 248, 240, 224, 192, 128]):
            return False

        return True
    except:
        return False


def isPrivate(item):
    a = [int(i) for i in item[0]]
    if a[0] == 10:
        return True
    elif a[0] == 172 and 31 < a[1] < 32:
        return True
    elif a[0] == 192 and a[1] == 168:
        return True
    return False


arr = []
while True:
    try:
        s = input()
        arr.append([i.split(".") for i in s.split("~")])
    except:
        break
#      A,B,C,D,E,Err,Private
ans = [0, 0, 0, 0, 0, 0, 0]

for i, v in enumerate(arr):
    is_legal = isLegal(v)
    if is_legal is None:
        continue
    if is_legal:
        a = [int(i) for i in v[0]]
        if a[0] <= 126:
            ans[0] += 1
        elif a[0] <= 191:
            ans[1] += 1
        elif a[0] <= 223:
            ans[2] += 1
        elif a[0] <= 239:
            ans[3] += 1
        else:
            ans[4] += 1

        if isPrivate(v):
            ans[6] += 1
    else:
        ans[5] += 1
print(" ".join([str(i) for i in ans]))
