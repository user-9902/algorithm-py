"""
@title:      226. 翻转二叉树
@difficulty: 简单
@importance: 5/5
@tags:       递归
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        @tags:              递归
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       左子树 是 右子树的镜像， 右子树 是 左子树的镜像
        """
        if root is not None:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)
        return root
