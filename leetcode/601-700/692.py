"""
@title:      692. 前K个高频单词
@difficulty: 中等
@importance: 3/5
@tags:       sort hashmap
"""

from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        @tags:              sort hashmap
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        """
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1

        res = [(dic[k], k) for k in dic]
        res.sort(key=lambda x: (-x[0], x[1]))
        return [res[i][1] for i in range(k)]
