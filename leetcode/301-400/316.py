"""
@title:      316. 去除重复字母
@difficulty: 中等
@importance: 4/5
@tags:       hash 贪心
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        @tags:              hash
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       遍历字符，确定当前字符能否放在队尾。
        """
        left = Counter(s)  # 统计每个字母的出现次数
        ans = []  # 当作栈
        in_ans = set()
        for c in s:
            left[c] -= 1
            if c in in_ans:  # ans 中不能有重复字母
                continue
            # (设 x=ans[-1]) 如果 c < x，且右边还有 x，那么可以把 x 去掉，
            # 因为后面可以重新把 x 加到 ans 中
            while ans and c < ans[-1] and left[ans[-1]]:
                in_ans.remove(ans.pop())  # 标记栈顶不在 ans 中
            ans.append(c)  # 把 c 加到 ans 的末尾
            in_ans.add(c)  # 标记 c 在 ans 中
        return ''.join(ans)
