"""
@title:      390. 消除游戏
@difficulty: 中等
@importance: 
@tags:       约瑟夫环
"""

from typing import List, Iterable, Optional
from collections import deque


class Node:
    def __init__(self, val, next: Optional[Node] = None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(iter: Iterable):
        for i in iter:
            print(i)


class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        @tags:              链表 模拟删除过程
        @time complexity:   O(2n)
        @space complexity:  O(n)
        @description:       
        """
        pass

    def lastRemaining(self, n: int) -> int:
        """
        @tags:              math
        @time complexity:   O(2n)
        @space complexity:  O(n)
        @description:       
        """
        def ysf(n, k, i):
            if i == 1:
                return (n + k - 1) % n
            else:
                return ysf(n-1, k, i-1) % n
        return ysf(n, 2, n)
