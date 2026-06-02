"""
@title:      147. 对链表进行插入排序
@difficulty: 中等
@importance: 3/5
@tags:       链表 插入排序
"""

from typing import Optional
from math import inf


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        tmp = ListNode(-inf)
        while cur:
            # 暂存下一个节点
            next_cur = cur.next
            cur.next = None

            a = tmp
            # 寻找插入节点
            while a.next and cur.val > a.next.val:
                a = a.next
            if a.next:
                b = a.next
                a.next = cur
                cur.next = b
            else:
                a.next = cur
            cur = next_cur

        return tmp.next
