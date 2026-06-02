"""
@title:      650. 只有两个键的键盘
@difficulty: 中等
@importance: 5/5
@tags:       dp math
"""


class Solution:
    def minSteps(self, n: int) -> int:
        """
        @tags:              math
        @time complexity:   O(sqrt(2))
        @space complexity:  O(n)
        @description:       n 由于n的最大因数复制而来的步长最小，复制的步长=n的最小因数
        """
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = float("inf")

            j = 1
            while j * j <= i:
                # 到达i需要先到达j，如果j不是i的因数的话，从j是无法到达i的 如 3 无法到达 8
                if i % j == 0:
                    # 因数都是成对的 所以上面枚举至 j * j <= i, 来减少枚举次数
                    # 到达 j 的步骤 + j 到达 i的步骤
                    f[i] = min(f[i], f[j] + i // j, f[i // j] + j)
                j += 1

        return f[n]

    def minSteps(self, n: int) -> int:
        """
        @tags:              math 💲质因数分解
        @time complexity:   O(sqrt(2))
        @space complexity:  O(1)
        @description:       同上方的解 这里压缩到一维了 同时更能体现出数学意涵。
        """
        ans = 0
        i = 2
        while i*i <= n:
            # 寻找最小因数
            while n % i == 0:
                n //= i
                ans += i    # 需要复制的次数
            i += 1
        # 无法再质因分解
        if n > 1:
            ans += n
        return ans
