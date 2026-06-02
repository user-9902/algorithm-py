"""
@title:      HJ50 四则运算
@difficulty: 困难
@importance: 4/5
@tags:       dfs
"""
import re

s = '3+2*{1+2*[-4/(8-6)+7]}'


def calu(s):
    stack = []
    result = []
    temp = []

    for i, char in enumerate(s):
        if char == '{':
            if not stack:
                start = i  # 记录起始位置
            stack.append(char)
        elif char == '}':
            if stack:
                stack.pop()
                if not stack:
                    end = i  # 记录结束位置
                    result.append((start, end, s[start+1:end]))
        elif stack:
            temp.append(char)

    return result


print(calu(s))
