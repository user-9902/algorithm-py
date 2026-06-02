"""
@title:      710. 黑名单中的随机数
@difficulty: 中等
@importance: 5/5
@tags:       前缀和 dp
"""

import bisect
from typing import List
import random


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        """
        @tags:              白名单
        @time complexity:   O(n)
        @space complexity:  O(n)    ❌ 空间复杂度超了
        @description:       创建白名单，在白名单中随机。
        """
        s = set(blacklist)
        arr = []
        for i in range(n):
            if i in s:
                continue
            arr.append(i)
        self.arr = arr

    def pick(self) -> int:
        n = len(self.arr)
        k = randint(0, n - 1)
        return self.arr[k]


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        """
        @tags:              白名单
        @time complexity:   O(n)
        @space complexity:  O(n)    ❌ 空间复杂度超了
        @description:       创建白名单，在白名单中随机。
        """
        blacklist.sort()
        left = []
        for i, v in enumerate(blacklist):
            if i == 0:
                if v == 0:
                    v += 1
                left.append(v)
            else:
                left.append(v - len(left))
        self.blacklist = blacklist
        self.left = left
        self.n = n

    def pick(self):
        """
        :rtype: int
        """
        k = random.randint(0, self.n - len(self.blacklist)-1)
        l = bisect.bisect_right(self.left, k)
        if l > 0 or k == 0:
            l = self.left[l-1]
        return k + l


Solution(3, [0]).pick()
