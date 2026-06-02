"""
@title:      236. 二叉树的最近公共祖先
@difficulty: 中等
@importance: 5/5
@tags:       后续dfs 标记 LCA
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        @tags:              后续dfs
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        def dfs(node):
            if node is None:
                return None
            l = dfs(node.left)
            r = dfs(node.right)
            c = node if node == p or node == q else None
            if (c and l) or (c and r) or (l and r):
                return node
            return l or r or c

        return dfs(root)
