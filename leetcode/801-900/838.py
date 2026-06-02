"""
@title:      838. 推多米诺
@difficulty: 简单
@importance: 4/5
@tags:       前缀最值
"""

from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        @tags:              前缀最值  
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       遍历 i 更具左侧最近的 R 和 右侧最近的 L 判断当前结束状态。解题过程类似接雨水
        """
        n = len(dominoes)
        leftR = [None] * n
        pre = None
        for i, v in enumerate(dominoes):
            if v == "R":
                pre = i
            elif v == "L":
                pre = None
            else:
                leftR[i] = pre

        res = ""
        post = None
        for i in range(n - 1, -1, -1):
            v = dominoes[i]
            if v == "L":
                post = i
                res = "L" + res
            elif v == "R":
                post = None
                res = "R" + res
            else:
                if leftR[i] is not None and post is not None:
                    if i - leftR[i] == post - i:
                        res = "." + res
                    elif i - leftR[i] > post - i:
                        res = "L" + res
                    else:
                        res = "R" + res
                elif leftR[i] is not None:
                    res = "R" + res
                elif post is not None:
                    res = "L" + res
                else:
                    res = "." + res
        return res


Solution().pushDominoes(".L.R...LR..L..")
