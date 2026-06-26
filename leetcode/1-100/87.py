"""
@title:      87. 扰乱字符串
@difficulty: 中等
@importance: 5/5
@tags:       记忆化搜索 dp
"""
from collections import Counter
from functools import cache


class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        @tags:              记忆化搜索
        @time complexity:   O(n^4)   
        @space complexity:  O(n^3)
        @description:       将问题切割为子问题即可。本题的记忆化搜索解更简单，且方便理解
        """
        n, m = len(s1), len(s2)

        # 边界条件
        if n != m:
            return False
        if Counter(s1) != Counter(s2):
            return False
        if s1 == s2:
            return True

        # 切割 重新判断
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        """
        @tags:              区间dp
        @time complexity:   O(n^3)   
        @space complexity:  O(n^3)
        @description:       将上述问题转化为dp
        """

        n = len(s1)
        if n != len(s2):
            return False

        # dp[i][j][k] 表示：
        # 从 s1 的第 i 个字符开始，长度为 k 的子串
        # 是否能通过扰乱得到
        # 从 s2 的第 j 个字符开始，长度为 k 的子串
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        # 初始化：长度为1的情况，只需要比较单个字符是否相等
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = (s1[i] == s2[j])

        # 枚举子串长度，从2到n
        for length in range(2, n + 1):
            # 枚举 s1 中子串的起始位置 i
            # i + length <= n，所以 i 最大为 n - length
            for i in range(n - length + 1):
                # 枚举 s2 中子串的起始位置 j
                for j in range(n - length + 1):
                    # 枚举切割点 k（左子串的长度）
                    for k in range(1, length):
                        # 情况1：没有交换左右子树
                        # 检查 s1[i:i+k] 和 s2[j:j+k] 是否匹配
                        # 且 s1[i+k:i+length] 和 s2[j+k:j+length] 是否匹配
                        if (dp[i][j][k] and dp[i + k][j + k][length - k]):
                            dp[i][j][length] = True
                            break  # 找到一种匹配方式就可以跳出循环
                        
                        # 情况2：交换了左右子树
                        # s1 的左部分对应 s2 的右部分
                        # s1 的右部分对应 s2 的左部分
                        # 
                        # s1[i:i+k] 与 s2[j+length-k:j+length] 匹配（长度 k）
                        # s1[i+k:i+length] 与 s2[j:j+length-k] 匹配（长度 length-k）
                        if (dp[i][j + length - k][k] and dp[i + k][j][length - k]):
                            dp[i][j][length] = True
                            break  # 找到一种匹配方式就可以跳出循环
        
        # 最终答案：整个字符串 s1[0:n] 和 s2[0:n] 是否能通过扰乱得到
        return dp[0][0][n]
