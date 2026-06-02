"""
@title:      25. K 个一组翻转链表
@difficulty: 中等
@importance: 4/5
@tags:       链表
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        @tags:              链表
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       💲画图，分析过程
        """
        cur = head
        ans = None
        p = None
        while cur:
            f = cur

            # 计算有没有 k 个数
            cnt = 0
            t = cur
            for _ in range(k):
                if cur:
                    cur = cur.next
                    cnt += 1

            # 反转
            pre = None
            if cnt == k:
                for _ in range(k):
                    tmp = t.next
                    t.next = pre
                    pre = t
                    t = tmp

            # 前面反转后的尾巴
            if p:
                p.next = pre if cnt == k else f
            p = f

            # 结果记录
            if ans is None:
                ans = pre if cnt == k else f
        return ans


b = ListNode(5)
c = ListNode(4, b)
d = ListNode(3, c)
e = ListNode(2, d)
f = ListNode(1, e)
Solution().reverseKGroup(f, 3)
