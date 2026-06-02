"""
@title:      515. 在每个树行中找最大值
@difficulty: 中等
@importance: 1/5
@tags:       bfs
"""
from typing import List, Optional
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              bfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       bfs 同 leetcode 117 无需二外空间存储层级
        """
        queue = [root]
        res = []
        if root is None:
            return res

        while queue:
            maxVal = -inf
            n = len(queue)
            for _ in range(n):
                cur = queue.pop(0)
                maxVal = max(cur.val, maxVal)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(maxVal)
        return res
