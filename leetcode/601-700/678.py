"""
@title:      678. 有效的括号字符串
@difficulty: 中等
@importance: 5/5
@tags:       dp 栈 greedy
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        @tags:              区间dp
        @time complexity:   O(n^2)   
        @space complexity:  O(n^2)
        @description:       如下注释
        """
        n = len(s)
        f = [[False] * n for _ in range(n)]

        # 初始化单个字符的有效性
        for i in range(n):
            f[i][i] = s[i] == "*"  # 单个字符总是有效的

        # 初始化两个字符的情况
        for i in range(1, n):
            if s[i] in {")", "*"} and s[i - 1] in {"(", "*"}:
                f[i - 1][i] = True

        # 处理大于两个字符的子串
        for step in range(2, n):    # 依次处理长度为 3，4，5 ... n
            for l in range(n - step):
                # s[l] s[r] 左右匹配 f[l+1][r-1] = true 则 f[l][r] = true
                if (
                    s[l] in {"(", "*"}
                    and s[l + step] in {")", "*"}
                    and f[l + 1][l + step - 1]
                ):
                    f[l][l + step] = True
                # f[l][k] = true f[k+1][r] = true 则 f[l][r] = true
                for k in range(l, l + step):
                    if f[l][k] and f[k + 1][l + step]:
                        f[l][l + step] = True
                        break

        return f[0][n - 1]

    def checkValidString(self, s: str) -> bool:
        """
        @tags:              栈 greedy
        @time complexity:   O(n)   
        @space complexity:  O(1)
        @description:       记录栈中左括号数量的范围
        """
        minC = 0    # 最少多少左括号
        maxC = 0    # 最多多少左括号
        for i in s:
            if i == '(':
                minC += 1
                maxC += 1
            elif i == ')':
                minC = max(0,  minC - 1)
                maxC -= 1
                if maxC < 0:
                    return False
            else:
                minC = max(0, minC - 1)  # 星号可以匹配 左括号
                maxC += 1

        return minC == 0
