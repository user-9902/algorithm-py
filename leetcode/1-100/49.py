"""
@title:      49. 字母异位词分组
@difficulty: 简单
@importance: 4/5
@tags:       hashmap
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        @tags:              hashmap
        @time complexity:   O(nmlogm)
        @space complexity:  O(nm)
        @desc:              异位字符串的共性就是，按字母表排序后相同。
        """
        dic = defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))  # 找到合适的键值
            dic[k].append(s)
        return list(dic.values())
