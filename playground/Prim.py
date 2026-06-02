"""
@title:      Prim
@difficulty: 中等
@importance: 6/5
@tags:       Prim 最小生成树
"""

"""
Prim 算法用以解决最小生成子树的问题

从节点入手
假设从节点A出发
将节点A视为一个整体，剩余所有节点视为一个整体
取连接A和剩余节点的最小权值的边，即可
然后将A和最小权值的边连接的节点视为一个新的整体，再次将剩余节点视为另一个整体即可
"""




import heapq
def prim(graph: dict, start: int) -> int:
    """
    使用 Prim 算法找到从 start 开始的最小生成树的总权重。

    参数:
    graph: 字典形式的邻接表，键为顶点编号，值为该顶点指向其他顶点的边及其权重。
    start: 开始构建最小生成树的起始顶点编号。

    返回:
    最小生成树的总权重。
    """
    n = len(graph)
    visited = set()  # 记录已访问过的顶点
    total_weight = 0  # 最小生成树的总权重
    heap = [(0, start)]  # 优先队列，存储待处理的边（权重, 目标顶点）

    while heap:
        weight, node = heapq.heappop(heap)  # 取出最小权重的边
        if node not in visited:
            visited.add(node)
            total_weight += weight
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (edge_weight, neighbor))

    return total_weight


# 示例
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

start_vertex = 0
mst_weight = prim(graph, start_vertex)
print(f"MST Weight starting from vertex {start_vertex}: {mst_weight}")
