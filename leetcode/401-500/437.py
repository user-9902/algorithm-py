"""
name:       437. 路径总和 III
difficulty: 简单
importance: 3/5
tags:       dfs
"""

from types import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        @tags:              后续dfs
        @time complexity:   O(n)
        @space complexity:  O(n^2)
        """
        ans = 0

        def dfs(node):
            nonlocal ans
            if node is None:
                return []
            l = dfs(node.left)
            r = dfs(node.right)

            res = [node.val]
            for v in r:
                res.append(node.val + v)
            for v in l:
                res.append(node.val + v)
            for v in res:
                if v == targetSum:
                    ans += 1
            return res
        dfs(root)
        return ans
