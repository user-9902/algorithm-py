"""
@title:      661. 图片平滑器
@difficulty: 中等
@importance: 4/5
@tags:       业务分析
"""

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        @tags:              遍历
        @time complexity:   O(n*m)
        @space complexity:  O(n*m)
        @description:       业务分析题，细心处理边界条件即可
        """
        n, m = len(img), len(img[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                l = 0 if j == 0 else j - 1
                r = m if j == m-1 else j + 2
                t = 0 if i == 0 else i-1
                b = n if i == n-1 else i + 2
                s = 0
                for a1 in range(t, b):
                    for a2 in range(l, r):
                        s += img[a1][a2]
                ans[i][j] = s // ((r - l) * (b - t))
        return ans
