"""
@title:      HJ37 统计每个月兔子的总数
@difficulty: 简单
@importance: 5/5
@tags:       递归 斐波那契额数列 线性代数
"""


"""
@tags:              递推
@time complexity:   O(n)
@space complexity:  O(n)
@description:       斐波那契额数列
"""
n = int(input())

f = [0] * n
for i in range(0, n):
    if i < 2:
        f[i] = 1
    else:
        f[i] = f[i-2] + f[i-1]
print(f[n-1])


"""
@tags:              递推
@time complexity:   O(n)
@space complexity:  O(1)
@description:       斐波那契额数列 空间优化
"""
n = int(input())

a = 1   # 能生兔子的兔子
b = 0   # 不能生育的兔子
c = 0   # 刚出生的兔子
for i in range(3, n+1):
    a += b
    b = c
    c = a
print(a+b+c)


"""
@tags:              递推
@time complexity:   O(logn)
@space complexity:  O(1)
@description:       线性代数
"""

