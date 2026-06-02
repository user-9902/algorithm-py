"""
@title:      68. 文本左右对齐
@difficulty: 中等
@importance: 4/5
@tags:       边界分析
"""

"""
应用题
向 cur 中不断加入字符串, 
    当前字符串的加入: 未超过了最大限制 继续
                     超过最大限制 cur加入结果数组, cur=""
    最后一行特殊处理
"""




from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)

        left = 0
        right = 0
        s_total = 0
        for i in range(n):
            cur_s = words[i]
            cur_len = len(cur_s)

            if s_total + right - left + cur_len > maxWidth:
                # 生成一行
                space = maxWidth - s_total

                if right - left == 1:
                    words.append(words[left] + ' ' * space)
                else:
                    space_min = space // (right - left - 1)
                    space_rest = space % (right - left - 1)
                    for j in range(left, right - 1):
                        words[j] += ' '*space_min
                        if space_rest:
                            words[j] += ' '
                            space_rest -= 1
                    words.append(''.join(words[left:right]))
                left = i
                right = i + 1
                s_total = cur_len
            else:
                # 还能装下
                s_total += cur_len
                right += 1

        if right <= n:
            for i in range(left, right - 1):
                words[i] += ' '
            words.append(''.join(words[left:n]) + ' ' *
                         (maxWidth - s_total - right + left+1))

        return words[n:]
