"""
@title:      47. 全排列 II
@difficulty: 简单
@importance: 4/5
@tags:       回溯
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        @tags:              回溯算法 位运算优化 剪枝
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        @description:       同leetcode 46 多了一步剪枝
        """
        n = len(nums)
        u = (1 << n) - 1
        ans = []
        cur = []

        def dfs(s):
            if s == 0:
                ans.append(cur.copy())
            st = set()
            for i in range(n):
                c = 1 << i
                if (c & s) and nums[i] not in st:
                    st.add(nums[i])
                    cur.append(nums[i])
                    dfs(s ^ c)
                    cur.pop()

        dfs(u)
        return ans
