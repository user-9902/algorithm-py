"""
@title:      HJ107 求解立方根
@difficulty: 中等
@importance: 5/5
@tags:       二分
"""


def foo(num: float):
    if num == 0:
        return 0.0
    if num == 1:
        return 1.0
    if num == -1:
        return -1.0

    is_minus = num < 0
    num = abs(num)

    left = 0 if num < 1 else 1
    right = 1 if num < 1 else num
    mid = (left + right) / 2

    low = num - 0.001
    high = num + 0.001

    cur = mid * mid * mid
    while not low <= cur <= high:
        if cur < low:
            left, mid = mid, (mid + right) / 2
        elif cur > high:
            mid, right = (mid + left) / 2, mid
        else:
            raise NotImplementedError
        cur = mid * mid * mid

    if is_minus:
        mid = -mid

    return round(mid, 1)


print(foo(float(input())))
