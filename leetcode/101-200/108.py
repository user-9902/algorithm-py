"""
@title:      108. 将有序数组转换为二叉搜索树
@difficulty: 简单
@importance: 4/5
@tags:       二叉平衡树
"""

# Definition for a binary tree node.
from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        @tags:              dfs dp
        @time complexity:   O(n)
        @space complexity:  O(n)    调用栈开销
        @desc:              取中点即可，满足高低差<=1
        """
