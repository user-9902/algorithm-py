"""
@title:      919. 完全二叉树插入器
@difficulty: 简单
@importance: 4/5
@tags:       二叉树
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    """
    @tags:              满二叉树
    @time complexity:   init O(n) insert O(1) 
    @space complexity:  init O(n) insert O(1)
    @description:       利用满二叉树的性质快速找到父节点
    """

    def __init__(self, root: Optional[TreeNode]):
        nodes = []
        stack = [root]

        while stack:
            cur = stack.pop(0)
            if cur == None:
                continue
            nodes.append(cur)
            stack.append(cur.left)
            stack.append(cur.right)

        self.n = len(nodes) # 可以只记录n 这样插入的时间复杂度就是 logn 了
        self.nodes = nodes

    def insert(self, val: int) -> int:
        # 利用二叉树的特性实现 O(1) 插入复杂度
        node = TreeNode(val)
        self.nodes.append(node)
        n = self.n
        fid = (self.n - 1) // 2  # 父节点id
        if n > 0:
            if n % 2 == 0:
                self.nodes[fid].right = node
            else:
                self.nodes[fid].left = node
        self.n += 1
        return self.nodes[fid].val

    def get_root(self) -> Optional[TreeNode]:
        return None if self.n == 0 else self.nodes[0]
