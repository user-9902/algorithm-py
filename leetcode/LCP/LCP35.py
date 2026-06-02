"""
@title:      LCP 35. 电动车游城市
@difficulty: 困难
@importance: 4/5
@tags:       分层图最短路
"""

from typing import List
from math import inf
from heapq import heappop, heappush


class Solution:
    def electricCarPlan(
        self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]
    ) -> int:
        n = len(charge)
        graph = [[] for _ in range(n)]

        # 构建邻接表
        for u, v, cost in paths:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        # 初始化距离数组和访问数组
        distance = [[inf] * (cnt + 1) for _ in range(n)]
        visited = [[False] * (cnt + 1) for _ in range(n)]

        # 堆，存储 (总花费, 当前电量, 当前节点)
        hq = [(0, 0, start)]
        distance[start][0] = 0

        while hq:
            w, c, node = heappop(hq)

            if visited[node][c]:
                continue

            visited[node][c] = True

            # 遍历邻居节点
            for nxt, cost in graph[node]:
                if c >= cost and not visited[nxt][c - cost]:
                    cost2 = w + cost
                    if cost2 < distance[nxt][c - cost]:
                        distance[nxt][c - cost] = cost2
                        heappush(hq, (cost2, c - cost, nxt))

            # 原地充电
            if c < cnt and not visited[node][c + 1]:
                cost2 = w + charge[node]
                if cost2 < distance[node][c + 1]:
                    distance[node][c + 1] = cost2
                    heappush(hq, (cost2, c + 1, node))

        # 返回到达终点的最小花费
        return min(distance[end])
