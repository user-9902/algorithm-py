"""
@title:      337. 打家劫舍 III
@difficulty: 中等
@importance: 5/5
@tags:       dp dfs
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        @tags:              dfs dp
        @time complexity:   O(n)
        @space complexity:  O(n)    
        @description:       同打家劫舍I一样，当前节点可以选，可以不选。
                            max(i)= 当前节点不选 + 左子树最大值 + 右子树最大值
                                    当前节点选 + 左子树不选根节点 + 右子树不选根节点
        """
        # 后序遍历
        def dfs(node):
            # 终止条件
            if node is None:
                return 0, 0
            # 深度优先
            l_root, l_not_root = dfs(node.left)
            r_root, r_not_root = dfs(node.right)
            # 返回 选择当前节点的最大值，不选择当前节点的最大值
            return l_not_root + r_not_root + node.val, max(l_root, l_not_root) + max(r_root, r_not_root)

        return max(dfs(root))
