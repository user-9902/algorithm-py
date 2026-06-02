from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        pre = [0] + stones
        for i in range(1, n+1):
            pre[i] += pre[i-1]
        print(pre)
        f = []
        dfs(0, n-1, 1):
            


Solution.mergeStones([3, 2, 4, 1], 2)
