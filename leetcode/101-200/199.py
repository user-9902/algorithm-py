"""
@title:      199. 二叉树的右视图
@difficulty: 简单
@importance: 3/5
@tags:       BFS
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              递归
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       广度优先遍历，取最右侧的数字即可
        """
        # 实现省略