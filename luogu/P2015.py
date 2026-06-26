"""
@title:      P2015 二叉苹果树
@difficulty: 中等
@importance: 5/5
@tags:       树形背包
"""

n, k = 5, 2
arr = [
    [1, 3, 1],
    [1, 4, 10],
    [2, 3, 20],
    [3, 5, 20]
]
m = len(arr)
# 链式前向星存下数据
class Node {
    __init__(id){
        self.id = id
        self.child = []
    }
}

cap, n = [int(i) for i in input().split()]

groups = {}
for i in range(n):
    w, v, g = [int(i) for i in input().split()]
    if g not in groups:
        groups[g] = []
    groups[g].append([w, v])

groups = [groups[v] for i, v in enumerate(groups)]
group_num = len(groups)
f = [[0] * (cap + 1) for _ in range(group_num + 1)]
for i in range(1, group_num+1):
    for j in range(1, cap + 1):
        f[i][j] = f[i-1][j]
        for weight, value in groups[i-1]:
            if j >= weight:
                f[i][j] = max(f[i][j], f[i-1][j-weight] + value)
print(f[group_num][cap])
