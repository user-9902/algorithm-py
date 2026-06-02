"""
@title:      23. 合并 K 个升序链表
@difficulty: 中等
@importance: 5/5
@tags:       链表 优先队列 分治 排序
"""


from typing import List, Optional
from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _merge_two_list(self, la: Optional[ListNode], lb: Optional[ListNode]) -> Optional[ListNode]:
        if la is None or lb is None:
            return la or lb

        setry = ListNode()  # 头节点守卫
        curr = setry
        while la and lb:
            if la.val <= lb.val:
                curr.next = la
                la = la.next
            else:
                curr.next = lb
                lb = lb.next
            curr = curr.next

        curr.next = la or lb
        return setry.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        @tags:              链表
        @time complexity:   O(nk^2) n为数字的个数
        @space complexity:  O(1)
        @description:       将问题切割为合并两个有序链表，还可以再使用分治优化减少重复遍历的次数
        """
        setry = ListNode()  # 守卫节点
        for l in lists:
            if l:
                setry.next = self._merge_two_list(setry.next, l)
        return setry.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        @tags:              优先队列
        @time complexity:   O(nlogk) n为数字的个数
        @space complexity:  O(k)
        @description:       小根堆
        """
        ListNode.__lt__ = lambda a, b: a.val < b.val    # 💲py魔法方法

        h = [i for i in lists if i]
        heapify(h)

        tmp = head = ListNode()

        while h:
            node = heappop(h)
            head.next = node
            head = head.next
            node = node.next
            if node:
                heappush(h, node)
        return tmp.next
