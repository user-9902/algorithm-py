"""
@title:      417. 太平洋大西洋水流问题
@difficulty: 中等
@importance: 5/5
@tags:       dfs bfs
"""


from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        @tags:              bfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       起点状态是不明确的，终点状态是明确的，因此逆向思考，
        """
        n, m = len(heights), len(heights[0])

        f = [[0] * m for i in range(n)]
        stack = []
        for i in range(m):
            stack.append([0, i])
        for i in range(n):
            stack.append([i, 0])
        while stack:
            x, y = stack.pop()
            if f[x][y] == 0:
                f[x][y] = 1
                if x < n - 1 and heights[x][y] <= heights[x+1][y]:
                    stack.append([x+1, y])
                if y < m - 1 and heights[x][y] <= heights[x][y+1]:
                    stack.append([x, y + 1])
                if x > 0 and heights[x][y] <= heights[x-1][y]:
                    stack.append([x-1, y])
                if y > 0 and heights[x][y] <= heights[x][y-1]:
                    stack.append([x, y - 1])

        ans = []
        f2 = [[0] * m for i in range(n)]
        for i in range(m):
            stack.append([n-1, i])
        for i in range(n):
            stack.append([i, m-1])
        while stack:
            x, y = stack.pop()
            if f2[x][y] == 0:
                f2[x][y] = 1
                if x < n - 1 and heights[x][y] <= heights[x+1][y]:
                    stack.append([x+1, y])
                if y < m - 1 and heights[x][y] <= heights[x][y+1]:
                    stack.append([x, y + 1])
                if x > 0 and heights[x][y] <= heights[x-1][y]:
                    stack.append([x-1, y])
                if y > 0 and heights[x][y] <= heights[x][y-1]:
                    stack.append([x, y - 1])
                if f[x][y] == 1:
                    ans.append([x, y])
        return ans


Solution().pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
