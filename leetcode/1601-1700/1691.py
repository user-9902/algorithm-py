"""
@title:      1691. 堆叠长方体的最大高度
@difficulty: 困难
@importance: 5/5
@tags:       sort dp
"""
from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        """
        @tags:              dp sort
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       见下方分析
        """
        n = len(cuboids)
        for i in cuboids:
            i.sort()
        cuboids.sort()

        # f[i] i为底座时的最大高度
        f = [cuboids[i][2] for i in range(n)]
        f[0] = cuboids[0][2]
        for i in range(n):
            for j in range(i):
                # j 能 i 上面
                if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1] and cuboids[i][2] >= cuboids[j][2]:
                    f[i] = max(f[i], f[j] + cuboids[i][2])
        return max(f)
