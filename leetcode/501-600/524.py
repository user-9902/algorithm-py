"""
@title:      524. 通过删除字母匹配到字典里最长单词
@difficulty: 简单
@importance: 3/5
@tags:       sort 双指针 dp
"""

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """
        @tags:              双指针 sort
        @time complexity:   O(n^k)
        @space complexity:  O(1)
        @description:       检查dictionary中的元素是否是s的字串+判断是否是最长的字串
        """
        # 根据题意，长度相同的时候按字母顺序取最小的，需要我们先进行下排序
        # 这里可以优化 sort sort(key=lambda x: (-len(s), s)) 然后下方遍历也可以据此优化
        dictionary.sort()

        n = len(s)
        res = ""
        for dic in dictionary:
            p = 0
            for i in range(n):
                if s[i] == dic[p]:
                    p += 1
                    if p == len(dic):
                        if len(dic) > len(res):
                            res = dic
                        break
        return res

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """
        @tags:              dp
        @time complexity:   O(n^k)
        @space complexity:  O(1)
        @description:       检查dictionary中的元素是否是s的字串+判断是否是最长的字串
        """
        pass
