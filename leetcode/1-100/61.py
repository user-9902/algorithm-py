"""
@title:      61. 旋转链表
@difficulty: 简单
@importance: 5/5
@tags:       快慢指针 链表
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head
        l = 0
        while tmp:
            l += 1
            tmp = tmp.next
        if l == 1 or l == 0:
            return head

        k = k % l
        if k == 0:
            return head

        fast = slow = head
        while fast and fast.next:
            fast = fast.next
            if k <= 0:
                slow = slow.next
            k -= 1
        res = slow.next
        fast.next = head
        slow.next = None
        return res
