"""
@title:      934. 最短的桥
@difficulty: 中等
@importance: 3/5
@tags:       bfs
"""
from typing import List


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        @tags:              bfs
        @time complexity:   O(n)    双端bfs可优化性能
        @space complexity:  O(n)
        @description:       
        """
        n = len(grid)
        queue = []
        q2 = []
        for i in range(n):
            if q2:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    grid[i][j] = -1
                    while queue:
                        x, y = queue.pop(0)
                        q2.append([x, y])
                        for a, b in dirs:
                            if -1 < x + a < n and -1 < y + b < n and grid[x+a][y+b] == 1:
                                queue.append([x + a, y+b])
                                grid[x + a][y + b] = -1
                    break
        res = 0
        while q2:
            m = len(q2)
            for _ in range(m):
                x, y = q2.pop(0)
                for a, b in dirs:
                    if -1 < x + a < n and -1 < y + b < n:
                        if grid[x + a][y + b] == 0:
                            q2.append([x + a, y+b])
                            grid[x + a][y + b] = -1
                        if grid[x + a][y + b] == 1:
                            return res
            res += 1


Solution().shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])
