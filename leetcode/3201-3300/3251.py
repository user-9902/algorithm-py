from typing import List
from itertools import accumulate


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        m = max(nums)
        f = [[0] * (m + 1) for _ in range(n)]
        for j in range(nums[0] + 1):
            f[0][j] = 1
        for i in range(1, n):
            s = list(accumulate(f[i - 1]))  # f[i-1] 的前缀和
            for j in range(nums[i] + 1):
                max_k = j + min(nums[i - 1] - nums[i], 0)
                f[i][j] = s[max_k] % MOD if max_k >= 0 else 0
        return sum(f[-1][:nums[-1] + 1]) % MOD


Solution().countOfPairs([2, 3, 2])
