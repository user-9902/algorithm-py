"""
@title:      420. 强密码检验器
@difficulty: 中等
@importance: 5/5
@tags:       业务分析
"""
import re


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        """
        @tags:              业务分析
        @time complexity:   
        @space complexity:  
        @description:       分析有多少字符串是不用动的，有多少字符串是一定要动的
        """
        n = len(password)
        # 不需要变的
        keep = 0
        if len(re.findall('[a-z]', password)) > 0:
            keep += 1
        if len(re.findall('[A-Z]', password)) > 0:
            keep += 1
        if len(re.findall('\d', password)) > 0:
            keep += 1
        # 连续相同字符串
        change = []
        idx = 1
        while idx < n:
            c = 1
            while idx < n and password[idx] == password[idx - 1]:
                c += 1
                idx += 1
            if c > 2:
                change.append(c)
            idx += 1
        # 优先将 需要修改的字符串 修改为 keep

        # 需要删除时，优先删除连续字符串
        if n > 20:
            res = 0
            while n > 20 and change:
                cur = change[0] - 2
                n
        # 需要添加字符串时，优先添加keep
        elif n < 6:

            # keep > 0 修改 to_change =
        to_change = 0
        dele = n - 20
        while change and dele > n:
            cur = change[0] // 3
            if cur < dele:
                change.pop(0)
                dele -= cur
            else:
                to_change += cur - dele
        while change:
            to_change += change[0] // 3
            change.pop(0)
        res = 0
        if dele > 0:
            res += dele
        if to_change > 0:
            res += to_change
        if n < 6:
            res += 3 - keep
            n += 3 - keep
        return res


Solution().strongPasswordChecker("aaaaaaccccc")
