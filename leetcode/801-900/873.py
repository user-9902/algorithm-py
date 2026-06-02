"""
@title:      873. 最长的斐波那契子序列的长度
@difficulty: 中等
@importance: 5/5
@tags:       dp hashmap
"""
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        @tags:              dp hashmap
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       如果 i 能和 j组成数列，则j需要其前缀 i-j 
        """
        n = len(arr)
        f = [{} for _ in range(n)]

        ans = 1
        for i in range(1, n):
            for j in range(i):
                if arr[i] - arr[j] in f[j]:
                    # 保持斐波那契的特性 数列长度+1
                    f[i][arr[j]] = f[j][arr[i] - arr[j]] + 1
                else:
                    # 不能保持 初始化新数列 j i 的长度 2
                    f[i][arr[j]] = 2
                ans = max(ans, f[i][arr[j]])

        return ans if ans > 2 else 0
