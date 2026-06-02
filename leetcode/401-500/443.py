"""
@title:      443. 压缩字符串
@difficulty: 简单
@importance: 3/5
@tags:       模拟
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        @tags:              原地替换
        @time complexity:   O(n)   
        @space complexity:  O(n)
        """
        n = len(chars)

        c = chars[0]
        cnt = 1
        k = 0
        for i in range(1, n):
            if chars[i] != chars[i-1]:
                chars[k] = c
                k += 1
                if cnt > 1:
                    for j, v in enumerate(str(cnt)):
                        chars[k] = v
                        k += 1
                c = chars[i]
                cnt = 1
            else:
                cnt += 1
        # rest
        chars[k] = c
        k += 1
        if cnt > 1:
            for j, v in enumerate(str(cnt)):
                chars[k] = v
                k += 1
        return k
