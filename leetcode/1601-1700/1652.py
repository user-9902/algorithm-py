"""
@title:      1652. 拆炸弹
@difficulty: 中等
@importance: 3/5
@tags:       滑动窗口 前缀和
"""

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(n)
        """
        n = len(code)
        code2 = code * 2
        pre = [0] * (2 * n)
        pre[0] = code[0]
        for i in range(1, 2 * n):
            pre[i] = pre[i - 1] + code2[i]
        if k > 0:
            for i in range(n - 1, -1, -1):
                pre[i + k] -= pre[i]
            return pre[k: k + n]
        elif k < 0:
            for i in range(2 * n - 1, n - 1, -1):
                pre[i - 1] -= pre[i - 1 + k]
            return pre[n - 1: 2 * n - 1]
        else:
            return [0] * n

    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        @tags:              滑动窗口
        @time complexity:   O(n)
        @space complexity:  O(n)
        """
        code2 = code * 2  # 寻找窗口的范围，移动窗口
        pass
