"""
@title:      117. 填充每个节点的下一个右侧节点指针 II
@difficulty: 中等
@importance: 5/5
@tags:       bfs
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        """
        @tags:              bfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       bfs
        """
        queue = [root]
        while queue:
            pre = None
            n = len(queue)
            # 💲bfs 独立的遍历每一层 无需额外空间存储层级
            for _ in range(n):
                cur = queue.pop(0)
                if cur is None:
                    continue
                if pre:
                    pre.next = cur
                pre = cur
                queue.append(cur.left)
                queue.append(cur.right)
        return root
