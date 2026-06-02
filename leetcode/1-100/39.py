"""
@title:      39. 组合总和
@difficulty: 简单
@importance: 4/5
@tags:       回溯
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        @tags:              回溯
        @time complexity:   O(S) 其中 S 为所有可行解的长度之和
        @space complexity:  O(target) 
        @description:       枚举的所以可能
        """
        n = len(candidates)
        ans = []
        cur = []

        def dfs(i, pre):
            if pre >= target:
                if pre == target:
                    ans.append(cur.copy())
                return

            for j in range(i, n):
                cur.append(candidates[j])
                dfs(j, pre + candidates[j])
                cur.pop()

        dfs(0, 0)
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        @tags:              完全背包
        @time complexity:   O(S) 其中 S 为所有可行解的长度之和
        @space complexity:  O(target)
        @description:       完全背包解法
        """
        n = len(candidates)
        ans = []
        cur = []

        def dfs(i, pre):
            if i == n:
                return
            if pre >= target:
                if pre == target:
                    ans.append(cur.copy())
                return

            # 不选
            dfs(i+1, pre)
            # 选
            cur.append(candidates[i])
            dfs(i, pre + candidates[i])
            cur.pop()

        dfs(0, 0)
        return ans
