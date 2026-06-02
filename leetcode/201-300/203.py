"""
@title:      203. 移除链表元素
@difficulty: 简单
@importance: 5/5
@tags:       链表
"""
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        @tags:              链表
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       遍历链表删除val节点即可，💲用"守卫"来使得头节点的处理和后续节点的处理一致。
        """
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
