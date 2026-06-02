"""
@title:      463. 岛屿的周长
@difficulty: 中等
@importance: 5/5
@tags:       bfs
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        @tags:              洪水填充
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       见注释
        """
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = []
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    grid[i][j] = 2
                    while queue:
                        x, y = queue.pop(0)
                        for a, b in dirs:
                            if -1 < x + a < n and -1 < y + b < m and grid[x+a][y+b] == 1:
                                queue.append([x+a, y+b])
                                grid[x+a][y+b] = 2
                        for a, b in dirs:
                            # 到达边界
                            if -1 < x + a < n and -1 < y + b < m:
                                if grid[x+a][y+b] == 0:
                                    res += 1
                            # 周围无元素同到达边界
                            else:
                                res += 1
                    return res


Solution().islandPerimeter(
    [[1, 1], [1, 1]])
