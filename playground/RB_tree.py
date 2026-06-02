"""
红黑树
AVL tree 通过保证自身的平衡，使得其拥有很高的查找效率，
avl tree 的平衡是用插入、删除数据时的时间复杂度来换取的。
因此 avltree 更适用于频繁查找的场景。
rbtree 的诞生就为了兼顾查找效率和插入删除效率，rbtree保证了最长路径不超过最短路径的两倍。
rbtree 满足以下特性：
    节点是红色或黑色
    根节点是黑色
    叶子节点都是黑色
    红色节点的子节点、父节点都是黑色（从根节点到任意叶子节点的路径上不能有连续两个红色节点）
    从任意节点到达叶子节点的路径上包含相同的黑色节点（注意，rbtree中的叶子节点，指的是存在空子节点的节点）

参考：https://blog.csdn.net/cy973071263/article/details/122543826
"""

from typing import Optional

COLOR = ('black', 'red')
RED = ('\033[32m' '\033[0m')


class TreeNode:
    def __init__(self, val: Optional[int] = None):
        self.val = val
        self.left = None
        self.right = None
        self.color = COLOR[1]
        pass

    def __str__(self):
        # windows vscode code runner 插件输出中 打印不出颜色 开个控制台就好了
        s = '%s' % self.val
        if self.color == COLOR[1]:
            s = "\033[31m%s\033[0m" % s
        return s


class RB_tree:
    def __init__(self, val: int):
        pass

    @staticmethod
    def is_rbtree(cls, root) -> bool:
        if root.root:
            root = root.root


n = TreeNode(123)
print(n)
