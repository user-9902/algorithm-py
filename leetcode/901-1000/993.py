"""
@title:      993. 二叉树的堂兄弟节点
@difficulty: 中等
@importance: 3/5
@tags:       dfs
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        @tags:              dfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       遍历技巧 + 剪枝
        """
        # 返回 高度 和 父节点
        target_deep = None
        target_father = None

        def dfs(node, father, deep):
            nonlocal target_deep, target_father
            if node is None or (target_deep and deep > target_deep):
                return False

            if node.val == x or node.val == y:
                if target_deep is None:
                    target_deep = deep
                    target_father = father
                else:
                    return target_father != father and target_deep == deep

            return dfs(node.left, node, deep + 1) or dfs(node.right, node, deep + 1)

        return dfs(root, None, 0)
