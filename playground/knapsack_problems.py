"""
@title:      背包问题
@difficulty: 中等
@importance: 6/5
@tags:       dp
"""


# ---------------------------------------- 0-1背包 -----------------------------------------------
"""
1. 01背包

背包问题的金典的动态规划模型，背包问题都是在01背包的基础上做延申。
dp也称为递推，dp本质上解决了递归中，栈开销、栈溢出的问题。
01背包递归：
    对于第i个物品我们可以选择将其装进或不装进背包
    从上方的分析中，我们得到下面三个式子
        当前物品 i: dfs(i, cap)  
        不选当前物品 i：dfs(i-1, cap) 
        选当前物品 i：dfs(i-1, cap-val[i])
    下方的题解，展示了如何处理三个式子的关系，以及如何从递归 → 递推
"""




from typing import List
from functools import cache
def knapsack(w: List[int], v: List[int], cap: int):
    """
    @tags:              递归 记忆化搜索
    @time complexity:   O(m*n)
    @space complexity:  O(m*n)
    @description:       递归
    """
    n = len(w)

    @cache  # 优化下复杂度
    def dfs(i, c):
        if i < 0:
            return 0
        if c < w[i]:
            # 装不下了 无法选
            return dfs(i-1, c)
            # 下标为i的不选     下标为i的选
        return max(dfs(i-1, c), dfs(i-1, c - w[i]) + v[i])

    return dfs(n-1, cap)


def knapsack(w: List[int], v: List[int], cap: int):
    """
    @tags:              dp
    @time complexity:   O(m*n)
    @space complexity:  O(m*n)
    @description:       dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])

                           cap1 2 3 4 5
                        v w   0 0 0 0 0
                        7 5 0 0 0 0 0 7
                        5 3 0 0 0 5 5 7
                        1 2 0 0 1 5 5 7
                cap 表示背包容量 w 表示重量 v表示价值
    """
    n = len(w)
    f = [[0] * (cap + 1) for _ in range(n+1)]

    # 枚举物品
    for i in range(1, n+1):
        # 枚举背包容量
        for j in range(i, cap+1):
            f[i][j] = f[i-1][j]  # 不选
            # 能装得下
            if j - w[i-1] >= 0:
                f[i][j] = max(f[i][j], f[i-1][j - w[i-1]] + v[i-1])  # 不选 选

    return f[n][cap]


def knapsack(w: List[int], v: List[int], cap: int):
    """
    @tags:              dp
    @time complexity:   O(m*n)
    @space complexity:  O(m)
    @description:       空间优化，观察上方的二维数组，可以发现 f[i][j] 的状态依赖于 f[i-1]列中<=的部分

        [i-1][0]...[i-1][j]
                   [i ][j]
        从图形中可以看出依赖是数据是上左放的数据，所有可以将其压缩为 1 维
    """
    n = len(w)
    # 💲压缩空间复杂度不是固定的解题技巧。具体问题具体分析，需要观察状态间的依赖关系来压缩。
    f = [0] * (cap + 1)

    for i in range(1, n+1):
        for j in range(cap, w[i-1] - 1, -1):
            f[j] = max(f[j], f[j - w[i-1]] + v[i-1])

    return f[cap]


# ----------------------------------------- 完全背包问题 -----------------------------------------------

"""
2. 完全背包问题

01背包进阶问题，01背包中只能选或不选，完全背包中可选多次k(0 < k < j/w[i])次
因此状态转移方程
dp[i][j] = max(dp[i-1][j], dp[i-1][j - k*w[i]] + k*v[i])
"""


def unbounded_knapsack_dp(w: List[int], v: List[int], cap: int):
    """
    @tags:              递归
    @time complexity:   O(m*n)
    @space complexity:  O(m*n)
    @description:       朴素递归
    """
    n = len(w)

    @cache
    def dfs(i, cap):
        if i == n:
            return 0
        if cap < w[i]:
            return dfs(i+1, cap)
        return max(dfs(i+1, cap), dfs(i, cap-w[i]) + v[i])
    return dfs(0, cap)


def unbounded_knapsack_dp(w: List[int], v: List[int], cap: int) -> int:
    """
    @tags:              dp
    @time complexity:   O(m*n)
    @space complexity:  O(m*n)
    @description:       递推
    """
    n = len(w)
    f = [[0]*(cap+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(1, cap+1):
            f[i+1][j] = f[i][j]
            if j >= w[i]:
                f[i+1][j] = max(f[i+1][j], f[i+1][j-w[i]] + v[i])
    return f[n][cap]


def unbounded_knapsack_dp(w: List[int], v: List[int], cap: int):
    """
    @tags:              dp
    @time complexity:   O(m*n)
    @space complexity:  O(m)
    @description:       空间压缩，f[i][j]依赖上方相邻、左侧的数据
    """
    n = len(w)
    f = [0]*(cap+1)

    for i in range(n):
        for j in range(w[i], cap+1):
            f[j] = max(f[j], f[j-w[i]] + v[i])
    return f[cap]


# ----------------------------------------- 多重背包 -----------------------------------------------
"""
3.多重背包问题

01背包中，物品的数量为1
完全背包中，物品的数量为inf
而多重背包中，物品的数量为k(0 < k < inf)
"""


def multi_knpstack(w: List[int], v: List[int], c: List[int], cap: int):
    """
    转化为完全背包
    dp[i][j] = max(dp[i-1][j], dp[i-1][j - k*w[i]] + k*v[i]) | k < j/w[i] & & k < c[i]
    """
    n = len(w)
    f = [[0] * (cap + 1)for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, cap+1):
            f[i][j] = f[i-1][j]
            for k in range(j // w[i-1] + 1):
                if k <= c[i - 1]:
                    f[i][j] = max(f[i][j], f[i-1][j-k*w[i-1]] + k*v[i-1])
    return f[n][cap]


def multi_knpstack(w: List[int], v: List[int], c: List[int], cap: int):
    """
    dp
    同样可以压缩为一维
    """
    n = len(w)
    f = [0] * (cap + 1)

    for i in range(1, n+1):
        for j in range(cap, w[i-1] - 1, -1):
            for k in range(1, min(c[i-1], j // w[i-1]) + 1):
                f[j] = max(f[j], f[j - k * w[i-1]] + k * v[i-1])
    return f[cap]


# ----------------------------------------- 分组背包 -----------------------------------------------
"""
4.分组背包
在01背包的基础上，对物品进行分组，每组内的物品只能选一个
"""


def group_knapsack(cap: int, groups: List[List[int]]):
    group_num = len(groups)
    f = [[[0] * (cap + 1)] for _ in range(group_num + 1)]
    # 因为同一组内的物品只能选一个，我们将一组数据视为01背包中的一个物体
    for i in range(1, group_num+1):
        for j in range(1, cap + 1):
            f[i][j] = f[i-1][j]
            # 遍历这组的数据
            for weight, value in groups[i-1]:
                if j >= weight:
                    f[i][j] = max(f[i][j], f[i-1][j-weight] + value)
    return f[group_num][cap]


def group_knapsack(cap: int, groups: List[List[int]]):
    """
    压缩为一维的方式同01背包
    """
    group_num = len(groups)
    f = [0] * (cap + 1)
    # 因为同一组内的物品只能选一个，我们将一组数据视为01背包中的一个物体
    for i in range(1, group_num+1):
        for j in range(cap, -1, -1):
            # 遍历这组的数据
            for weight, value in groups[i-1]:
                if j >= weight:
                    f[j] = max(f[j], f[j-weight] + value)
    return f[cap]
