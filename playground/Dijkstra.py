"""
@title:      Dijkstra
@difficulty: 中等
@importance: 6/5
@tags:       greedy
"""

"""
最短路径问题

"""




from math import inf
from typing import List
def dijkstra(matrix: List[List[int]], start: int, end: int) -> int:
    """
    greedy
    从根节点出发，维护最短路径列表
    从最短路径列表中挑选出最短的路径，选出下一个节点
    """
    n = len(matrix)
    # 到达对应节点的最短距离，前一个节点
    res = [[inf, None] for _ in range(n)]
    fin = [False] * n

    res[start][0] = 0
    res[start][1] = start
    fin[start] = True

    cur = start
    while True:
        # 更新 res
        for i, v in enumerate(matrix[cur]):
            if v == inf or v == 0 or fin[i]:
                continue
            res[i][0] = min(res[i][0], v + res[cur][0])
            res[i][1] = cur
        # 找寻res中的最小路径
        min_i = None
        for x, y in enumerate(res):
            if fin[x] or y[0] == inf:
                continue
            if min_i is None or res[min_i][0] > y[0]:
                min_i = x
        # 下一轮的工作
        if min_i == None:
            break
        fin[min_i] = True
        cur = min_i
        # 得到end的最短即可停止
        if min_i == end:
            break

    return res[end][0]
