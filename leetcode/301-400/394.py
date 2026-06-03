"""
@title:      394. 字符串解码
@difficulty: 中等
@importance: 5/5
@tags:       dfs 栈 业务模拟
"""

import re


class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(leng, s):
            num_len = 0
            left = None
            n = 0
            res = ""
            for i, c in enumerate(s):
                if c == "[":
                    if n == 0:
                        left = i
                    n += 1
                elif c == "]":
                    n -= 1
                    if n == 0:
                        res += dfs(int(s[left - num_len: left]),
                                   s[left + 1: i])
                        num_len = 0
                elif re.match(r"[a-z]", c) and n == 0:
                    res += c
                elif re.match(r"[0-9]", c) and n == 0:
                    num_len += 1
            return leng * res
        return dfs(1, s)
    
# 下方是js版本
# var decodeString = function(s) {
#     //  @tags:              栈
#     //  @time complexity:   O(n)
#     //  @space complexity:  O(n)
#     //  @description:       字符串后可能跟数字 [前一点有数字
#     const numStack = []
#     const strStack = []
#     let currentStr = ''
#     let currentNum = 0
    
#     for (let i = 0; i < s.length; i++) {
#         const c = s[i]
        
#         if (c >= '0' && c <= '9') {
#             // 累积数字（可能有多位）
#             currentNum = currentNum * 10 + (c - '0')
#         } 
#         else if (c >= 'a' && c <= 'z') {
#             // 累积字符串
#             currentStr += c
#         }
#         else if (c === '[') {
#             // 遇到 '['，将当前数字和字符串压栈，然后重置
#             numStack.push(currentNum)
#             strStack.push(currentStr)
#             currentNum = 0
#             currentStr = ''
#         }
#         else if (c === ']') {
#             // 遇到 ']'，弹出栈顶，重复字符串
#             const repeatTimes = numStack.pop()
#             const prevStr = strStack.pop()
#             currentStr = prevStr + currentStr.repeat(repeatTimes)
#         }
#     }
    
#     return currentStr
# }


Solution().decodeString("3[a]2[bc]")
