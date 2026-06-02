"""
@title:      923. 三数之和的多种可能
@difficulty: 中等
@importance: 5/5
@tags:       sort dp
"""

from typing import List
from collections import Counter
from functools import cache


class Solution:
    """
    本题为三数之和改
    """

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        @tags:              递归
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)  ❌空间复杂度超了 需改为递推
        @description:       01背包
        """
        n = len(arr)

        @cache
        def dfs(i, target, cnt):
            if i == n:
                return 1 if target == 0 and cnt == 3 else 0

            # 不选 + 选
            return dfs(i + 1, target, cnt) + dfs(i + 1, target - arr[i], cnt + 1)

        return dfs(0, target, 0) % (10**9 + 7)

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        @tags:              递推
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       01背包
        """
        MOD = 10 ** 9 + 7

        n = len(arr)
        f = [[[0] * 4 for _ in range(target + 1)] for _ in range(n + 1)]
        f[0][0][0] = 1
        for i in range(n):
            f[i][0][0] = 1
            for j in range(target + 1):
                for k in range(1, 4):
                    # 不选
                    f[i+1][j][k] = f[i][j][k]
                    if j >= arr[i]:
                        f[i+1][j][k] = (f[i+1][j][k] + f[i]
                                        [j - arr[i]][k - 1]) % MOD
        return f[n][target][3]

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        @tags:              sort
        @time complexity:   O(nm)
        @space complexity:  O(n)
        @description:       三数之和解
        """
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        res = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            t = target - arr[i]
            if t < 2 * arr[l] or t > 2 * arr[r]:
                continue
            while l < r:
                if arr[l] + arr[r] < t:
                    l += 1
                elif arr[l] + arr[r] > t:
                    r -= 1
                else:
                    if arr[l] == arr[r]:
                        res += (r - l) * (r - l + 1) // 2
                        break
                    else:
                        l += 1
                        r -= 1
                        cntl = 1
                        cntr = 1
                        while arr[l] == arr[l - 1]:
                            l += 1
                            cntl += 1
                        while arr[r] == arr[r + 1]:
                            r -= 1
                            cntr += 1
                        res += cntl * cntr
        return res % MOD
