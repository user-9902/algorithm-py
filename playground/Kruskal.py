"""
@title:      Kruskal
@difficulty: 中等
@importance: 6/5
@tags:       Kruskal 最小生成树
"""

"""
kruskal 算法用以解决最小生成子树的问题

从边入手
将图中所有的边按照权值从低到高排序
按权值从小到大将边填入图中，若新加入的边使得子树出现回路，则丢弃该条边
直至加入n-1条边时，子树便构建完成
"""




from typing import List
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(edges: List[List[int]], n: int) -> int:
    uf = UnionFind(n)
    edges.sort(key=lambda x: x[2])  # 按照边的权重排序

    mst_weight = 0
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight

    return mst_weight


# 示例
edges = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
]
n = 4  # 图中的顶点数

mst_weight = kruskal(edges, n)
print("MST Weight:", mst_weight)
