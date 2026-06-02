"""
@title:      24. 两两交换链表中的节点
@difficulty: 中等
@importance: 5/5
@tags:       链表
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        defend = ListNode()
        defend.next = head

        pre = a = b = defend

        while True:
            if a.next is None or a.next.next is None:
                break
            # 存在连续两个后续节点
            # 移动到对应位置
            pre = a
            a = pre.next
            b = a.next
            # 改动指针指向
            pre.next = b
            a.next = b.next
            b.next = a

        return defend.next
