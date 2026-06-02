from math import inf
from typing import List


def floyd(matrix: List[List[int]]):
    """
    dp
    依次以每个节点为中转节点，遍历每个节点，搜寻更短的路径
    """
    n = len(matrix)

    d = matrix.copy()
    p = [[i for i in range(n)] for _ in range(n)]

    # 依次把每个节点作为中间节点
    for i in range(n):
        # 遍历每个节点，搜寻是否存在更优路径
        for x in range(n):
            if x == i:
                continue
            for y in range(n):
                if y == i or x == y:
                    continue
                if d[x][y] > d[x][i] + d[i][y]:
                    d[x][y] = d[x][i] + d[i][y]
                    p[x][y] = i
    for i in p:
        print(i)
    return (d, p)


def bellman_ford():
    pass


test_matrix = [
    [0, 1, 5, inf, inf, inf, inf, inf, inf],
    [1, 0, 3, 7, 5, inf, inf, inf, inf],
    [5, 3, 0, inf, 1, 7, inf, inf, inf],
    [inf, 7, inf, 0, 2, inf, 3, inf, inf],
    [inf, 5, 1, 2, 0, 3, 6, 9, inf],
    [inf, inf, 7, inf, 3, 0, inf, 5, inf],
    [inf, inf, inf, 3, 6, inf, 0, 2, 7],
    [inf, inf, inf, inf, 9, 5, 2, 0, 4],
    [inf, inf, inf, inf, inf, inf, 7, 4, 0]
]

floyd(test_matrix)
