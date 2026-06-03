"""
@title:      679. 24 点游戏
@difficulty: 中等
@importance: 4/5
@tags:       DFS
"""
from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        @tags:              DFS 浮点误差
        @time complexity:   O(n! * 6^n)
        @space complexity:  O(n^2)
        @description:       如下注释
        """
        EPS = 1e-9  # 精度误差

        def dfs(cards2):
            n = len(cards2)
            if n == 1:
                return abs(cards2[0] - 24) < EPS
            # 随机挑两个数
            for i, x in enumerate(cards2):
                for j in range(i+1, n):
                    y = cards2[j]
                    # 加法乘法可互换位置、减法、除法不可以
                    r = [x + y, x * y, x - y, y - x]
                    # 除法还需保证分母不为0
                    if abs(y) > EPS:
                        r.append(x / y)
                    if abs(x) > EPS:
                        r.append(y / x)

                    # 深度遍历
                    n_cards2 = cards2[:j] + cards2[j+1:]
                    for v in r:
                        n_cards2[i] = v  # j 删掉 i 替换掉
                        if dfs(n_cards2):
                            return True
            return False
        return dfs(cards)
