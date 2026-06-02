"""
@title:      953. 验证外星语词典
@difficulty: 中等
@importance: 3/5
@tags:       sort
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        @tags:              hashmap
        @time complexity:   O(m*n)
        @space complexity:  O(m)
        @description:       
        """
        index = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            size = min(len(words[i - 1]), len(words[i]))
            for j in range(size):
                c1, c2 = index[words[i - 1][j]], index[words[i][j]]
                if c1 < c2:
                    break
                elif c1 > c2:
                    return False
                if j == size - 1 and size < len(words[i-1]):
                    return False
        return True


Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
