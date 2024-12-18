"""
@title:      146. LRU 缓存
@difficulty: 简单
@importance: 4/5
@tags:       数据结构 双线循环链表
"""


class Node:
    __slots__ = "pre", "nxt", "key", "val"

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node(-1, -1)
        self.dummy.pre = self.dummy
        self.dummy.nxt = self.dummy
        self.k = dict()

    def get(self, key: int) -> int:
        if key not in self.k:
            return -1
        node = self.k[key]
        self.remove(node)
        self.push(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        if val >= 0:
            self.k[key].val = value
            return

        self.k[key] = node = Node(key, value)
        self.push(node)
        if len(self.k) > self.capacity:
            back = self.dummy.pre
            del self.k[back.key]
            self.remove(back)

    def remove(self, node: Node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre

    def push(self, node: Node):
        node.pre = self.dummy
        node.nxt = self.dummy.nxt
        node.pre.nxt = node
        node.nxt.pre = node
