"""
@title:      138. 随机链表的复制
@difficulty: 中等
@importance: 4/5
@tags:       链表 map 
"""

"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        @tags:              map
        @time complexity:   O(n)
        @space complexity:  O(1)
        @desc:              复制链表的基础上，需要处理random。将新旧节电的映射关系存下来，即可。
        """
        # 实现忽略