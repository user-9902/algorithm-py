"""
@title:      3. 无重复字符的最长子串
@difficulty: 简单
@importance: 5/5
@tags:       haspmap 指针 滑动窗口
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # 获取索引 i
            dic[s[j]] = j  # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        @tags:              指针 滑动窗口
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       滑动窗口，确保窗口内的字母只出现一次。
        """
        dic = defaultdict(int)
        l = ans = 0
        for i, v in enumerate(s):
            dic[v] += 1
            if dic[v] > 1:
                if i - l > ans:
                    ans = i - l
                while dic[v] > 1:
                    dic[s[l]] -= 1
                    l += 1
        return max(ans, len(s) - l)
