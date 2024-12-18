"""
@title:      234. 回文链表
@difficulty: 简单
@importance: 3/5
@tags:       链表
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        @tags:              朴素解
        @time complexity:   O(n)
        @space complexity:  O(n)
        @desc:              转为数组解题
        """
        pass

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        @tags:              链表
        @time complexity:   O(n)
        @space complexity:  O(1)
        @desc:              链表中点 + 反转链表
        """
        fast = head
        slow = head
        pre = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt
        a = slow.next
        slow.next = pre
        b = slow
        # 奇偶判断
        if fast.next is None and fast != head:
            b = b.next
        while a:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True


a = ListNode(1, ListNode(2))
print(Solution().isPalindrome(a))
