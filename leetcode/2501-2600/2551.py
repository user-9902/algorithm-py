from typing import List


class Solution:
    def putMarbles(self, wt: List[int], k: int) -> int:
        for i in range(len(wt) - 1):
            wt[i] += wt[i + 1]
        print(wt)
        wt.pop()
        wt.sort()
        return sum(wt[len(wt) - k + 1:]) - sum(wt[:k - 1])


Solution().putMarbles([1, 3, 5, 1], 2)
