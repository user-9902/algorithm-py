"""
@title:      94. 二叉树的中序遍历
@difficulty: 简单
@importance: 5/5
@tags:       中序遍历
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              递归
        @time complexity:   O(n)
        @space complexity:  O(n)    调用栈开销
        @description:       中序的递归实现。对于一个树，先处理其左子树，再处理根节点，然后是右子树
        """
        res = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              迭代
        @time complexity:   O(n)
        @space complexity:  O(n)    栈的开销
        @description:       迭代相当于，手动实现递归中函数的调用栈
        """
        res = []
        stack = []
        cur: Optional[TreeNode] = root

        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            else:
                break
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              Morris
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       
        """
        res = []
        cur: Optional[TreeNode] = root

        while cur:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right is not None and pre.right != cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res


root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
root.left = a
root.right = b
a.left = c
a.right = d

Solution().inorderTraversal(root)
