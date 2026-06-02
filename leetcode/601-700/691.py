"""
name:       691. 贴纸拼词
difficulty: 简单
importance: 3/5
tags:       记忆化搜索 
"""
from typing import List
from functools import cache, reduce
from collections import Counter


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """
        @tags:              dfs
        @time complexity:   O(mn^2)
        @space complexity:  O(m+n)
        @description:       dfs+剪枝
        """
        s = set(reduce(lambda x, pre: pre + x, stickers))
        for i in target:
            if i not in s:
                return -1

        cnt = Counter(target)
        cnts = [Counter(s) for s in stickers]

        res = len(target) + 1

        def dfs(step):
            nonlocal res
            if step > res:
                return
            if all([cnt[k] <= 0 for k in cnt]):
                res = min(step, res)
                return

            for k in cnt:
                if cnt[k] > 0:
                    for i in cnts:
                        if k in i:
                            for x in i:
                                if x in cnt:
                                    cnt[x] -= i[x]
                            dfs(step + 1)
                            for x in i:
                                if x in cnt:
                                    cnt[x] += i[x]

        dfs(0)
        return res

Solution().minStickers(["with", "example", "science"], "thehat")
