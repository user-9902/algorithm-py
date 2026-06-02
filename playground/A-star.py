"""
A* 算法
"""

# import matplotlib.pyplot as plt

# plt.title("title")  # 括号当中输入标题的名称
# plt.grid()
# plt.xlim(0, 50)
# plt.ylim(0, 50)


# X = [[1, 2], [3, 4], [5, 6]]
# plt.imshow(X)
# plt.show()

from math import inf
from sortedcontainers import SortedList

"""
0表示未遍历
1表示遍历过了
9表示墙壁，既无法到达的点
"""
width = height = 8
matrix = [[9] * (width + 2), *[[9] + ([0] * width) + [9]
                               for _ in range(height)], [9] * (width + 2)]


def print_matrix(matrix=matrix):
    print('------------------------')
    for i in matrix:
        print(i)


def bfs(begin, target):
    """
    bfs
    在路径花费相同的时候，dijkstra会退化为bfs。
    """
    queue = [begin]

    while queue:
        cur = queue.pop(0)
        x, y = cur

        if cur == target:
            return True

        if matrix[x][y] != 0:
            continue

        matrix[x][y] = 1

        # 记录下父节点，即可知道路径
        queue.append([x, y+1])
        queue.append([x+1, y])
        queue.append([x, y-1])
        queue.append([x+1, y])

    return False


def best_first(begin, target):
    """
    best first search 最佳优先搜索
    bfs，遍历了很多的无效节点，因为没有方向性，很像人生不是么[doge],漫无目的，会很累哦。
    为了解决这个问题，bf算法加入方向的概念，既权值。
    """
    x, y = target
    cost = [[abs(i - x)] * (width + 2) for i in range(height+2)]
    for i in range(height+2):
        for j in range(width+2):
            if matrix[i][j] == 9:
                cost[i][j] = inf
            else:
                cost[i][j] += abs(y-j)

    # 优先队列
    queue = SortedList([(cost[begin[0]][begin[1]], begin)], key=lambda x: x[0])

    while queue:
        cur = queue.pop(0)[1]
        x, y = cur

        if cur == target:
            return True

        if matrix[x][y] != 0:
            continue

        matrix[x][y] = 1

        # 记录下父节点，即可知道路径
        queue.add((cost[x][y+1], [x, y+1]))
        queue.add((cost[x+1][y], [x+1, y]))
        queue.add((cost[x][y-1], [x, y-1]))
        queue.add((cost[x-1][y], [x-1, y]))

    return False


def get_manhattan_distance():
    """
    曼哈顿距离
    欧拉（Euler）距离需要开方，性能较差
    """
    
    pass


def a_star(begin, target):
    """
    a*
    best first 在有障碍的图中性能也没那么好了
    """

    pass

# bfs
# bfs([1, 1], [3, 7])
# print_matrix()

# 无障碍的 bf
# best_first([1, 1], [3, 7])
# print_matrix()


# 有障碍的 bf
# matrix[1][4] = 9
# matrix[2][4] = 9
# matrix[3][4] = 9
# matrix[4][4] = 9

# best_first([1, 1], [3, 7])
# print_matrix()
