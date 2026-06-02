"""
@title:      46. 全排列
@difficulty: 简单
@importance: 4/5
@tags:       回溯
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        @tags:              回溯算法 
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       记录每个元素的选取状况，取过的无法再取了
        """
        n = len(nums)
        ans = []
        status = [False] * n
        cur = [0] * n

        def dfs(idx):
            if idx == n:
                ans.append(cur.copy())
            for i in range(n):
                if not status[i]:
                    cur[idx] = nums[i]
                    # 确保不重复取
                    status[i] = True
                    dfs(idx + 1)
                    # 放开选取权限
                    status[i] = False

        dfs(0)
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        @tags:              回溯算法 + 位运算优化
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        """
        n = len(nums)
        u = (1 << n) - 1
        ans = []
        cur = []

        def dfs(s):
            if s == 0:
                ans.append(cur.copy())
            for i in range(n):
                c = 1 << i
                if c & s:
                    cur.append(nums[i])
                    dfs(s ^ c)
                    cur.pop()

        dfs(u)
        return ans
