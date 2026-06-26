"""
@title:      552. 学生出勤记录 II
@difficulty: 困难
@importance: 4/5
@tags:       dp
"""
from functools import cache


class Solution:
    def checkRecord(self, n: int) -> int:
        """
        @tags:              递归
        @time complexity:   O(n)
        @space complexity:  O(n)  ❌ 栈空间的复杂度会溢出。分析题意的复杂度范围，需转化为dp再压缩维度
        """
        MOD = 10**9 + 7

        @cache
        def dfs(i, pre, hasA):
            if i > 2 and pre[-3:] == "LLL":
                return 0
            if i == n:
                return 1
            if hasA:
                return dfs(i + 1, pre + "L", False) + dfs(i + 1, pre + "P", False)
            else:
                return (
                    dfs(i + 1, pre + "L", False)
                    + dfs(i + 1, pre + "P", False)
                    + dfs(i + 1, pre + "A", True)
                )

        return dfs(0, "", False) % MOD

    def checkRecord(self, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)     
        @space complexity:  O(n)
        @desc:              前置题 leetcode 122
        """
        MOD = 10 ** 9 + 7
        #   [[   无A             ],[ 有A            ]]
        #   [0l结尾 1l结尾 2l结尾]
        f = [[[0, 0, 0], [0, 0, 0]] for _ in range(n+1)]
        f[0][0][0] = 1

        for i in range(1, n+1):
            # p结尾
            for j in range(2):
                for k in range(3):
                    # 当前以p结尾，变成连续0天迟到
                    f[i][j][0] = (f[i][j][0] + f[i-1][j][k]) % MOD

            # l结尾
            for j in range(2):
                # 不能在2l结尾加l
                for k in range(1, 3):
                    # 当前以l结尾，迟到天数+1
                    f[i][j][k] = (f[i][j][k] + f[i-1][j][k-1]) % MOD

            # A结尾
            for k in range(3):
                # 当前以A结尾，只能添加到没迟到的结尾。
                # 同时注意迟到天数变为 0
                f[i][1][0] = (f[i][1][0] + f[i-1][0][k]) % MOD

        ans = 0
        for j in range(2):
            for k in range(3):
                ans += f[n][j][k]
        return ans % MOD

    def checkRecord(self, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)     
        @space complexity:  O(n)
        @description:       滚动数组压缩
        """
        MOD = 10 ** 9 + 7
        f = [[[0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0]]]
        f[0][0][0] = 1

        for i in range(1, n+1):
            cur = i % 2
            pre = (i - 1) % 2
            if i > 1:
                for j in range(2):
                    for k in range(3):
                        f[i][j][k] = 0
            # p结尾
            for j in range(2):
                for k in range(3):
                    f[cur][j][0] = (f[cur][j][0] + f[pre][j][k]) % MOD

            # l结尾
            for j in range(2):
                # 不能在2l结尾加l
                for k in range(1, 3):
                    f[cur][j][k] = (f[cur][j][k] + f[pre][j][k-1]) % MOD

            # A结尾
            for k in range(3):
                f[cur][1][0] = (f[cur][1][0] + f[pre][0][k]) % MOD

        ans = 0
        for j in range(2):
            for k in range(3):
                ans += f[n % 2][j][k]
        return ans
